from JSONSchemaCollision import possible_index_keys, schema_result_file
from JsonUtils import read_json_file, write_as_json_file

test_json_file = "edu.gov_2885_27.12.2011_recommended-books.json"
test_schema_file = schema_result_file


def process(json_file, schema_file):
    result = convert_json_by_schema(read_json_file(json_file),
                                    read_json_file(schema_file),
                                    null_value_as_empty_string=True)
    write_as_json_file("mapped_" + json_file, result)


def convert_json_by_schema(original_json, schema, null_value_as_empty_string=False):
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


def collect_index_with_options(result, key_options, input_dict):
    if any(x in possible_index_keys for x in input_dict.keys()):
        for key in list(input_dict):
            if key in possible_index_keys:
                index = input_dict[key]
                del input_dict[key]
                input_dict['key_options'] = list(set(key_options))
                result.update({index: input_dict})
    else:
        for key in input_dict:
            val = input_dict.get(key)
            if type(val) is dict:
                key_options.append(key)
                collect_index_with_options(result, key_options, val)
            elif type(val) is list:
                for content in val:
                    key_options.append(key)
                    collect_index_with_options(result, key_options, content)


process(test_json_file, test_schema_file)
