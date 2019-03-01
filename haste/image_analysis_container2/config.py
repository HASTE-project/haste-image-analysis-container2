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

# intervals are closed.
STORAGE_POLICY = [
    (0.0, 0.199999, 'move-to-trash'),
    (0.2, 1.0, 'move-to-my-dir'),
]

WINDOW_LENGTH = 10

STREAM_ID_INITIALS = 'ola-lab'

POLLING_INTERVAL_SECONDS = 5

LOGGING_LEVEL = logging.DEBUG
