import datetime
import logging
from itertools import groupby

from haste_storage_client.core import HasteStorageClient

from PIL import Image
import io
import numpy as np
from skimage.feature import greycomatrix, greycoprops
from skimage.filters import laplace

from haste.image_processor_2.azn_filenames import parse_azn_file_name
from haste.image_processor_2.image_analysis import extract_features

initials = 'ola'

# TODO: where will this come from? idle gap?
stream_id = datetime.datetime.today().strftime('%Y_%m_%d__%H_%M_%S') + '__' + initials
# stream_id = '2018_11_08__12_34_59_from_al'
hsc = HasteStorageClient(stream_id)

# TODO: file listing, pause, warning.

# TODO: dockerfile


def process_files(files, source_dir):
    files = list(map(lambda f: {'original_filename': f}, files))

    for f in files:

        # Check if file already processed.
        # TODO: eh? it shouldn't be here else
        result = hsc.mongo_collection.find_one()  # dict or None
        if result is not None:
            logging.error(f'file: {f["original_filename"]} already in mongodb?! should have been moved?')
            continue

        # TODO: parse filename in ola format:
        for k, v in parse_azn_file_name(f['original_filename']).items():
            f[k] = v

        # Load image from disk:
        with open(source_dir + '/' + f["original_filename"], mode='rb') as file:  # b is important -> binary
            image_bytes = file.read()

        # Takes ~0.02 secs for a couple MB file
        f["extracted_features"] = extract_features(image_bytes)
        # extracted_features = {
        #     'sum_of_intensities': int(np.sum(image)),
        #     'correlation': __corr(image),
        #     'laplaceVariance': __laplace_variance(image)
        # }

        # (discard image bytes)

        # print(f)

    keyfunc = lambda f: (f['well'], f['color_channel'])
    f_grped = groupby(sorted(files, key=keyfunc), key=keyfunc)

    for k, g in f_grped:
        # print(k, list(g))

        files_in_group = sorted(list(g), key = lambda f: f['time_point_number'])

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

            pass

    print('')
