import logging
import time

from itertools import groupby

from haste.image_analysis_container2.filenames.filenames import parse_filename
from haste.image_analysis_container2.fileutils import creation_date
from haste.image_analysis_container2.image_analysis import extract_features

fake_time_point_number = 0


def process_files(files, source_dir, hsc):
    global fake_time_point_number

    logging.info(f'found {len(files)} during polling.')

    files = list(map(lambda f: {'metadata': {'original_filename': f}}, files))

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
            logging.error(f["metadata"][
                              "original_filename"] + 'already in mongodb?! should have been moved? will overwrite metadata')

        # Load image from disk:
        f_full_path = source_dir + '/' + f['metadata']["original_filename"]
        with open(f_full_path, mode='rb') as file:  # b is important -> binary
            image_bytes = file.read()

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
            f['timestamp'] = f['metadata']['time_point_number']
        else:
            logging.debug('falling back to file modified time -- will likely be wrong for copied-in datasets')
            f['timestamp'] = creation_date(f_full_path)

            # for Polina's sample, there is no time dimension -- so as a hack, use the well sample
            f['time_point_number'] = fake_time_point_number
            fake_time_point_number += 1

        # (discard image bytes)

    # print(f)

    keyfunc = lambda f: (f['metadata']['well'], f['metadata']['color_channel'], f['metadata']['imaging_point_number'])
    s = sorted(files, key=keyfunc)
    f_grped = groupby(s, key=keyfunc)

    for k, g in f_grped:
        # print(k, list(g))

        files_in_group = sorted(list(g), key=lambda f: f['metadata']['time_point_number'])

        print(files_in_group)

        for f in files_in_group:
            logging.info(f'saving {f["metadata"]["original_filename"]}...')

            hsc.save(f['timestamp'],
                     (0, 0),
                     f['metadata']['well'],
                     bytearray(),  # empty, since we use the 'move file' storage driver.
                     f['metadata'])
