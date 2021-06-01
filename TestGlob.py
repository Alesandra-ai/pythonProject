import glob
import os

def test_glob():
    for file in glob.glob('test_data/input/csv/*'):
        with open(file, encoding='UTF-8') as file_read:
            print(file_read.read())


def test_os_list():
    for file_name in os.listdir('test_data/input/csv/'):
        with open(file_name, encoding='UTF-8') as file:
            print(file.read())


test_os_list()
