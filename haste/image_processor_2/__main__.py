import datetime

from haste_storage_client.core import HasteStorageClient

from haste.image_processor_2.config import SOURCE_DIR, STREAM_ID_INITIALS, WINDOW_LENGTH, HASTE_STORAGE_CLIENT_CONFIG, \
    STORAGE_POLICY
from haste.image_processor_2.foo import process_files
from haste.image_processor_2.model import KendallTauInterestingnessModel


def main():
    # TODO: where will this come from? idle gap?
    stream_id = datetime.datetime.today().strftime('%Y_%m_%d__%H_%M_%S') + '__' + STREAM_ID_INITIALS

    print(stream_id)


    model = KendallTauInterestingnessModel(WINDOW_LENGTH)
    hsc = HasteStorageClient(stream_id,
                             storage_policy=STORAGE_POLICY,
                             config=HASTE_STORAGE_CLIENT_CONFIG,
                             interestingness_model=model)

    # TODO: a loop

    files = [f'AssayPlate_NUNC_#165305-1_B02_T{i:04d}F001L01A01Z01C02.tif' for i in range(1, 10)]

    for f in files:
        process_files([f], SOURCE_DIR, hsc)


if __name__ == '__main__':
    main()
