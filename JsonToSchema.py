from genson import SchemaBuilder

from JsonUtils import read_json_file, write_as_json_file


# Make json schema from json content
def json_to_schema(json_content_file, result_file):
    schema_builder = SchemaBuilder()

    json_content = read_json_file(json_content_file)
    schema_builder.add_object(json_content)
    result_schema = schema_builder.to_schema()
    write_as_json_file(result_file, result_schema)
