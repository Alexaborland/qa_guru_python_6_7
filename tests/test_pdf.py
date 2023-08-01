from pypdf import PdfReader
import os
from .conftest import resources_path


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_by_pdf():
    reader = PdfReader(os.path.join(resources_path, "docs-pytest-org-en-latest.pdf"))
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)

    assert 412 == number_of_pages
    assert 'to' in text
