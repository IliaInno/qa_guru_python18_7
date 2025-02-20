import pytest, os.path, zipfile, shutil
from import_os_path import TMP_DIR, ARCHIVE_DIR, ZIP_DIR


@pytest.fixture(scope='session', autouse=True)
def create_archive():
    if not os.path.exists(ARCHIVE_DIR):
        os.mkdir(ARCHIVE_DIR)
    with zipfile.ZipFile(ZIP_DIR, 'w') as archive:
        for file in os.listdir(TMP_DIR):
            archive.write(os.path.join(TMP_DIR, file), file)

    yield
    shutil.rmtree(ARCHIVE_DIR)
