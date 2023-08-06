import os.path
import pytest

tmp_path = os.path.join(os.path.dirname((os.path.abspath(__file__))), '../tmp')
resources_path = os.path.join(os.path.dirname((os.path.abspath(__file__))), 'resources')


@pytest.fixture(scope='session', autouse=True)
def directory_management():
    files = os.listdir(tmp_path)
    for f in files:
        os.remove(os.path.join(tmp_path, f))
