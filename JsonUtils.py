import json

from genson import SchemaBuilder


def read_json_file(file_path):
    with open(file_path, encoding='UTF-8') as json_file:
        return json.loads(json_file.read())


def write_as_json_file(file_name, content):
    with open(file_name, 'w', encoding='UTF-8') as json_file:
        json_file.write(json.dumps(content, indent=4, ensure_ascii=False))


def json_to_schema(content):
    builder = SchemaBuilder()
    builder.add_schema(content)
    return builder.to_schema()
