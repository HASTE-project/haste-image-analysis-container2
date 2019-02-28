SOURCE_DIR = 'tests/images'

import os
from haste.image_processor_2.foo import process_files


def test_process_files():
    files = os.listdir(SOURCE_DIR)
    print(files)

    process_files(files, SOURCE_DIR)
