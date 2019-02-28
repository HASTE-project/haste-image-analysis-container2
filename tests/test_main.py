import datetime

from haste_storage_client.core import HasteStorageClient

from haste.image_processor_2.model import FooInterestingnessModel

SOURCE_DIR = 'tests/images'

import os
from haste.image_processor_2.foo import process_files


def test_process_files_one_batch():
    initials = 'deleteme'
    # TODO: where will this come from? idle gap?
    stream_id = datetime.datetime.today().strftime('%Y_%m_%d__%H_%M_%S') + '__' + initials
    # stream_id = '2018_11_08__12_34_59_from_al'

    model = FooInterestingnessModel()
    hsc = HasteStorageClient(stream_id, interestingness_model=model)

    files = os.listdir(SOURCE_DIR)
    print(files)

    process_files(files, SOURCE_DIR, hsc)


def test_process_files_multiple_batches_one_well():
    initials = 'deleteme'
    # TODO: where will this come from? idle gap?
    stream_id = datetime.datetime.today().strftime('%Y_%m_%d__%H_%M_%S') + '__' + initials

    print(stream_id)

    # stream_id = '2018_11_08__12_34_59_from_al'

    model = FooInterestingnessModel()
    hsc = HasteStorageClient(stream_id, interestingness_model=model)

    files = [f'AssayPlate_NUNC_#165305-1_B02_T{i:04d}F001L01A01Z01C02.tif' for i in range(1, 10)]

    for f in files:
        process_files([f], SOURCE_DIR, hsc)
