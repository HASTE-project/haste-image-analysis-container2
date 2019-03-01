import logging
import time

from itertools import groupby

from haste.image_analysis_container2.config import FILE_WRITE_GUARD_SECONDS
from haste.image_analysis_container2.filenames.filenames import parse_filename
from haste.image_analysis_container2.fileutils import file_modification_time
from haste.image_analysis_container2.image_analysis import extract_features
from haste.image_analysis_container2.kendall_tau_model import KEY_FUNC_GROUP, KEY_FUNC_SORT


def process_files(files, source_dir, hsc):
    logging.info(f'found {len(files)} during polling.')

    files = list(map(lambda f: {'metadata': {'original_filename': f}}, files))
    files_to_process = []

    for f in files:
        for k, v in parse_filename(f['metadata']['original_filename']).items():
            f['metadata'][k] = v

        # Warn if file already processed:
        result = hsc.mongo_collection.find_one({
            'metadata': {
                'original_filename': f['metadata']['original_filename']
            }
        })  # dict or None
        if result is not None:
            logging.error(f["metadata"]["original_filename"]
                          + 'already in mongodb?! should have been moved? will overwrite metadata')

        f_full_path = source_dir + '/' + f['metadata']["original_filename"]

        f['metadata']['file_modified_time_unix'] = file_modification_time(f_full_path)
        now = time.time()
        logging.debug(f"{f_full_path} was last modified {f['metadata']['file_modified_time_unix']}")
        logging.debug(f"its now {now}")

        if time.time() - f['metadata']['file_modified_time_unix'] < FILE_WRITE_GUARD_SECONDS:
            logging.info(
                f'skipping {f["metadata"]["original_filename"]} because mod in {FILE_WRITE_GUARD_SECONDS}s')
            continue

        with open(f_full_path, mode='rb') as f_contents:  # b is important -> binary
            image_bytes = f_contents.read()

        # Takes ~0.02 secs for a couple MB file
        t_start_image_ext = time.time()
        f['metadata']["extracted_features"] = extract_features(image_bytes)
        # extracted_features = {
        #     'sum_of_intensities': int(np.sum(image)),
        #     'correlation': __corr(image),
        #     'laplaceVariance': __laplace_variance(image)
        # }
        t_end_image_ext = time.time()
        f['metadata']['duration_image_extraction'] = t_end_image_ext - t_start_image_ext

        if 'time_point_number' in f['metadata']:
            # If we can get the time from the filename metadata, use it:
            # This is the timestamp used by HASTE
            f['timestamp'] = f['metadata']['time_point_number']
        else:
            logging.debug('falling back to file modified time -- will likely be wrong for copied-in datasets')
            # This is the timestamp used by HASTE
            f['timestamp'] = f['metadata']['file_creation_date']

            # This is the timestamp used for the interestingness model.
            # for Polina's sample, there is no time dimension.
            f['metadata']['time_point_number'] = 0

        # (image bytes are discarded)

        files_to_process.append(f)

    s = sorted(files_to_process, key=KEY_FUNC_GROUP)
    f_grped = groupby(s, key=KEY_FUNC_GROUP)

    for k, g in f_grped:
        files_in_group = sorted(list(g), key=KEY_FUNC_SORT)

        for f in files_in_group:
            logging.info(f'saving {f["metadata"]["original_filename"]}...')

            hsc.save(f['timestamp'],
                     (0, 0),  # no notion of location in this context.
                     f['metadata']['well'],
                     bytearray(),  # empty, since we use the 'move file' storage driver.
                     f['metadata'])
