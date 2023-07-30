import os.path
import requests
from .conftest import tmp_path


# TODO оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь
def test_download_png():
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'

    response = requests.get(url)
    with open('selenium_logo_square_green.png', 'wb') as file:
        file.write(response.content)

    size = os.path.getsize('selenium_logo_square_green.png')

    assert 30803 == size

