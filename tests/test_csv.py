import csv
import os.path

from .conftest import resources_path


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
def test_by_csv():
    with open(os.path.join(resources_path, 'resources/username.csv'), 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(os.path.join(resources_path, 'resources/username.csv')) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)
    assert len(row) == 3
