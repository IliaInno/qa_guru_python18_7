import os.path

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIR, "tmp")
ARCHIVE_DIR = os.path.join(CURRENT_DIR, "resources")
ZIP_DIR = os.path.join(ARCHIVE_DIR, 'archive.zip')