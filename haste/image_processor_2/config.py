SOURCE_DIR = 'TODO'
TARGET_DIR = 'TODO'

HASTE_STORAGE_CLIENT_CONFIG = {
    "haste_metadata_server": {
        "connection_string": "mongodb://???:?????@metadata-db-prod:27017/streams"
    },
    "log_level": "DEBUG",
    "targets": [
        {
            "id": "move-to-my-dir",
            "class": "haste_storage_client.storage.storage.MoveToDir",
            "config": {
                "source_dir": SOURCE_DIR,
                "target_dir": TARGET_DIR
            }
        }
    ]
}

# TODO: add 'trash' dir for PoC

STORAGE_POLICY = [(0.2, 1.0, 'move-to-my-dir')]

WINDOW_LENGTH = 10

STREAM_ID_INITIALS = 'ola-lab'
