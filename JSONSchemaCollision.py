from genson import SchemaBuilder

from JsonUtils import read_json_file, write_as_json_file

inputSchema = 'Schema1.json'
inputSchemaBase = 'Schema2.json'
schema_result_file = 'MergedSchemaResult.json'

possible_index_keys = ['id', 'index', 'indx', 'idx']


def merge_json_schemas(schema_base_file, schema_extra_file, merged_schema_file):
    schema_base = read_json_file(schema_base_file)
    schema_extra = read_json_file(schema_extra_file)

    schema_builder = SchemaBuilder()
    schema_builder.add_object({'index': 'String'})
    schema_builder.add_object({'key_options': ['String']})

    result_schema = schema_builder.to_schema()

    schema_base_index_lvl = get_index_lvl_dict(schema_base, remove_index=True)
    result_schema['properties'].update(schema_base_index_lvl)

    schema_extra_index_lvl = get_index_lvl_dict(schema_extra, remove_index=True)
    result_schema['properties'].update(schema_extra_index_lvl)

    write_as_json_file(merged_schema_file, result_schema)


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


merge_json_schemas(inputSchemaBase, inputSchema, schema_result_file)
