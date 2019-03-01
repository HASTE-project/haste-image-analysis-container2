import datetime
import logging
import os
import time

from haste_storage_client.core import HasteStorageClient

from haste.image_analysis_container2.config import SOURCE_DIR, STREAM_ID_INITIALS, WINDOW_LENGTH, \
    HASTE_STORAGE_CLIENT_CONFIG, \
    STORAGE_POLICY, LOGGING_LEVEL, LOGGING_FORMAT, LOGGING_FORMAT_DATE
from haste.image_analysis_container2.core import process_files
from haste.image_analysis_container2.kendall_tau_model import KendallTauInterestingnessModel


def main():
    logging.basicConfig(level=LOGGING_LEVEL,
                        format=LOGGING_FORMAT,
                        datefmt=LOGGING_FORMAT_DATE)

    # TODO: where will this come from? idle gap? from the filesystem? Recover if we die mid stream?
    stream_id = datetime.datetime.today().strftime('%Y_%m_%d__%H_%M_%S') + '__' + STREAM_ID_INITIALS

    logging.info(f'stream_id is: {stream_id}')

    model = KendallTauInterestingnessModel(WINDOW_LENGTH)
    hsc = HasteStorageClient(stream_id,
                             storage_policy=STORAGE_POLICY,
                             config=HASTE_STORAGE_CLIENT_CONFIG,
                             interestingness_model=model)

    logging.info('beginning polling loop...')
    while True:
        t_loop_start = time.time()

        t_listing_start = time.time()
        files = os.listdir(SOURCE_DIR)

        if len(files) > 0:
            logging.debug(f'Listing took: {time.time() - t_listing_start} secs')
            t_processing_start = time.time()
            process_files(files, SOURCE_DIR, hsc)
            logging.debug(f'Processing took: {time.time() - t_processing_start} secs')

        pause = time.time() - t_loop_start
        if pause < 0:
            logging.warn(f'Overran polling interval by {pause} seconds. Polling immediately.')
        else:
            time.sleep(pause)


if __name__ == '__main__':
    main()
