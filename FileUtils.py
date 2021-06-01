def write_to_file(path, content):
    with open(path, 'w', encoding='UTF-8') as file_to_write:
        file_to_write.write(content)


def read_file(path):
    with open(path, encoding='UTF-8') as file_to_read:
        return file_to_read.read()
