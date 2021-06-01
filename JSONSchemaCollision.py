from genson import SchemaBuilder

from JsonUtils import read_json_file, write_as_json_file

possible_index_keys = ['id', 'index', 'indx', 'idx']


def merge_json_schemas(base_schema_file, extra_schema_file):
    base_schema = read_json_file(base_schema_file)
    extra_schema = read_json_file(extra_schema_file)

    extra_schema_index_lvl = get_index_lvl_dict(extra_schema, remove_index=True)
    base_schema['properties'].update(extra_schema_index_lvl)

    write_as_json_file(base_schema_file, base_schema)


def make_base_schema(schema_path):
    schema_builder = SchemaBuilder()
    schema_builder.add_object({'index': 'String'})
    schema_builder.add_object({'key_options': ['String']})
    write_as_json_file(schema_path, schema_builder.to_schema())


def get_index_lvl_dict(input_dict, remove_index=False):
    result = {}

    search_index_lvl_dict(result, input_dict)

    if remove_index:
        for key in list(result):  # remove index a-like keys
            if key in possible_index_keys:
                del result[key]
    return result


def search_index_lvl_dict(result, input_dict):
    if any(x in possible_index_keys for x in input_dict.keys()):
        result.update(input_dict)
    else:
        for key in input_dict:
            if type(input_dict.get(key)) is dict:
                search_index_lvl_dict(result, input_dict.get(key))
