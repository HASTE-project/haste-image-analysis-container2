import logging

SOURCE_DIR = '/mnt/mikro-testdata/source/'
TARGET_DIR = '/mnt/mikro-testdata/target/'

HASTE_STORAGE_CLIENT_CONFIG = {
    "haste_metadata_server": {
        # In K8, this is the service name (since we're in the same namespace'
        "connection_string": "mongodb://mongodb:27017/streams"
        # "connection_string": "mongodb://mongodb.haste.svc.cluster:27017/streams"
    },
    "log_level": "DEBUG",
    "targets": [
        {
            "id": "move-to-keep",
            "class": "haste_storage_client.storage.storage.MoveToDir",
            "config": {
                "source_dir": SOURCE_DIR,
                "target_dir": TARGET_DIR + 'keep/'
            }
        },
        # For a PoC, trash is simply another dir:
        {
            "id": "move-to-trash",
            "class": "haste_storage_client.storage.storage.MoveToDir",
            "config": {
                "source_dir": SOURCE_DIR,
                "target_dir": TARGET_DIR + 'trash/'
            }
        }
    ]
}

# intervals are closed, and since we move the files, they can't overlap.
# TODO: this is a hack
STORAGE_POLICY = [
    (0.0, 0.199999999, 'move-to-trash'),
    (0.2, 1.0, 'move-to-keep'),
]

# Number of elements in the window over which to apply the model.
WINDOW_LENGTH = 10

STREAM_ID_INITIALS = 'ola-lab'

POLLING_INTERVAL_SECONDS = 10

LOGGING_LEVEL = logging.DEBUG
LOGGING_FORMAT = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
LOGGING_FORMAT_DATE = '%Y-%m-%d %H:%M:%S.%d3'
LOG_DIR = '/mnt/mikro-testdata/logs/'

