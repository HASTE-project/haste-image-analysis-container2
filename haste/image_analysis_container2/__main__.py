import datetime
import logging
import os
import time

from haste_storage_client.core import HasteStorageClient

from haste.image_analysis_container2.config import SOURCE_DIR, STREAM_ID_INITIALS, WINDOW_LENGTH, \
    HASTE_STORAGE_CLIENT_CONFIG, \
    STORAGE_POLICY, LOGGING_LEVEL
from haste.image_analysis_container2.core import process_files
from haste.image_analysis_container2.model import KendallTauInterestingnessModel


def main():
    LOGGING_FORMAT_DATE = '%Y-%m-%d %H:%M:%S.%d3'
    LOGGING_FORMAT = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'

    logging.basicConfig(level=LOGGING_LEVEL,
                        format=LOGGING_FORMAT,
                        datefmt=LOGGING_FORMAT_DATE)

    # TODO: where will this come from? idle gap? from the filesystem? Recover if we die mid stream?

    stream_id = datetime.datetime.today().strftime('%Y_%m_%d__%H_%M_%S') + '__' + STREAM_ID_INITIALS

    logging.log(f'stream_id is: {stream_id}')

    model = KendallTauInterestingnessModel(WINDOW_LENGTH)
    hsc = HasteStorageClient(stream_id,
                             storage_policy=STORAGE_POLICY,
                             config=HASTE_STORAGE_CLIENT_CONFIG,
                             interestingness_model=model)

    while True:
        t_loop_start = time.time()

        logging.info('polling for files...')
        t_listing_start = time.time()
        files = os.listdir(SOURCE_DIR)
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
