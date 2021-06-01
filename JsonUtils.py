import json

from FileUtils import read_file, write_to_file


def read_json_file(file_path):
    return json.loads(read_file(file_path))


def write_as_json_file(path, json_content):
    write_to_file(path, json_to_string(json_content))


def json_to_string(json_content):
    return json.dumps(json_content, indent=4, ensure_ascii=False)
