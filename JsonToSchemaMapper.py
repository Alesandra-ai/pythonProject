from JSONSchemaCollision import possible_index_keys
from JsonUtils import read_json_file, write_as_json_file


def convert_json_file(json_file, schema_file, result_path, null_value_as_empty_string=False):
    result = convert_json_by_schema(read_json_file(json_file),
                                    read_json_file(schema_file),
                                    null_value_as_empty_string)
    write_as_json_file(result_path, result)


def convert_json_by_schema(original_json, schema, null_value_as_empty_string):
    prepared_json = prepare_json(original_json)
    result = []
    for index in prepared_json:
        mid_result = {'index': index}
        index_dict = prepared_json[index]
        for prop in schema['properties']:
            if prop in possible_index_keys:
                continue
            if prop in index_dict:
                mid_result[prop] = index_dict[prop]
            elif null_value_as_empty_string:
                mid_result[prop] = ""
        result.append(mid_result)
    return result


def prepare_json(input_dict):
    key_options = []
    result = {}
    collect_index_with_options(result, key_options, input_dict)
    return result


def collect_index_with_options(result, key_options, input_data):
    if type(input_data) is dict:
        collect_index_with_options_dict(result, key_options, input_data)
    elif type(input_data) is list:
        for element in input_data:
            collect_index_with_options_dict(result, key_options, element)


def collect_index_with_options_dict(result, key_options, input_data):
    if any(x in possible_index_keys for x in input_data.keys()):
        for key in list(input_data):
            if key in possible_index_keys:
                index = input_data[key]
                del input_data[key]
                input_data['key_options'] = list(set(key_options))
                result.update({index: input_data})
    else:
        for key in input_data:
            val = input_data.get(key)
            if type(val) is dict:
                key_options.append(key)
                collect_index_with_options_dict(result, key_options, val)
            elif type(val) is list:
                for content in val:
                    key_options.append(key)
                    collect_index_with_options_dict(result, key_options, content)
