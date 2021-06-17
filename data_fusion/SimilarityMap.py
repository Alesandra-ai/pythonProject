import os
from difflib import SequenceMatcher

from JsonUtils import read_json_file, write_as_json_file


def make_similarity_map(json_folder, check_attr, result_map_path, allowance):
    result_map = {}

    for file in os.listdir(json_folder):
        append_map(read_json_file(json_folder + file), check_attr, result_map)

    collide_map = collide_map_by_similarity(result_map, allowance)

    write_as_json_file(result_map_path, collide_map)


def append_map(json_data, check_attr, result_map):
    for elem in json_data:
        if check_attr in elem:
            check_attr_val = elem[check_attr]
            if check_attr_val in result_map:
                result_map.get(check_attr_val).append(elem['index'])
            else:
                result_map[check_attr_val] = [elem['index']]


def collide_map_by_similarity(input_map, allowance):
    similarity_keys_map = {}
    for key in input_map:
        if not add_to_similar(key, input_map[key], similarity_keys_map, allowance):
            similarity_keys_map[key] = input_map[key]

    return similarity_keys_map


def add_to_similar(key, val, input_map, allowance):
    for candidate in input_map:
        if similar(key, candidate) >= allowance:
            # print("\"" + key + "\" similar to \"" + candidate + "\": " + str(similar(key, candidate)))
            input_map[candidate] += val
            return True


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
