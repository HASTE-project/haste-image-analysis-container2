import datetime
import logging
import time

import pymongo
from itertools import groupby

from haste_storage_client.core import HasteStorageClient

from PIL import Image
import io
import numpy as np
from skimage.feature import greycomatrix, greycoprops
from skimage.filters import laplace

from haste.image_analysis_container2.azn_filenames import parse_azn_file_name
from haste.image_analysis_container2.fileutils import creation_date
from haste.image_analysis_container2.image_analysis import extract_features


# TODO: file listing, pause, warning.

# TODO: dockerfile




def process_files(files, source_dir, hsc):
    files = list(map(lambda f: {'metadata': {'original_filename': f}}, files))

    for f in files:
        # TODO: parse filename in ola format:
        for k, v in parse_azn_file_name(f['metadata']['original_filename']).items():
            f['metadata'][k] = v

        # Check if file already processed.
        # TODO: eh? it shouldn't be here else
        result = hsc.mongo_collection.find_one({
            'metadata': {
                'original_filename': f['metadata']['original_filename']
            }
        })  # dict or None

        if result is not None:
            logging.error(f["metadata"][
                              "original_filename"] + 'already in mongodb?! should have been moved? willoverwrite metadata')

        #
        # assert 'well' in f['metadata']
        # assert 'color_channel' in f['metadata']
        # assert 'imaging_point_number' in f['metadata']

        # Load image from disk:
        f_full_path = source_dir + '/' + f['metadata']["original_filename"]
        with open(f_full_path, mode='rb') as file:  # b is important -> binary
            image_bytes = file.read()

        # Takes ~0.02 secs for a couple MB file
        t_start_image_ext = time.time()
        f['metadata']["extracted_features"] = extract_features(image_bytes)
        t_end_image_ext = time.time()
        f['metadata']['duration_image_extraction'] = t_end_image_ext - t_start_image_ext

        # extracted_features = {
        #     'sum_of_intensities': int(np.sum(image)),
        #     'correlation': __corr(image),
        #     'laplaceVariance': __laplace_variance(image)
        # }

        f['timestamp'] = creation_date(f_full_path)
        # TODO: (the above code is no good for testing -- since all the test files are modified at the same time
        f['timestamp'] = f['metadata']['time_point_number']

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
            # TODO: add the metadata for the group to the metadata
            # fetch the older ones as neceesary from mongodb
            # then call the HSC to invoke the model

            # interestingness model:
            # for sum, and correlation,
            #   kendals tau?
            #   linear regression?
            # then abs
            # then sub sampling/interlacing?
            # (note: laplaceVariance is a focus measure -- a check, not a trend)

            # TODO: add a driver which moves files on disk

            logging.info(f'saving {f["metadata"]["original_filename"]}...')
            hsc.save(f['timestamp'],
                     (0, 0),
                     f['metadata']['well'],
                     bytearray(),  # TODO
                     f['metadata'])


print('')
