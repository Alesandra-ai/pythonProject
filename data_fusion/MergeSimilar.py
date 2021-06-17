import os
from JsonUtils import read_json_file, write_as_json_file


def collect_ignore_ids(similarity_map):
    ignore = []
    for key in similarity_map:
        ignore += similarity_map[key][1::]
    return ignore


def merge_json(json, ignore_ids, merged_result, ignored_result):
    for elem in json:
        if elem['index'] not in ignore_ids:
            merged_result.append(elem)
        else:
            ignored_result.append(elem)


def merge_similar_by_map(json_folder, similarity_map_path, merged_result_path, ignored_result_path):
    merged_result = []
    ignored_result = []

    ignore_ids = collect_ignore_ids(read_json_file(similarity_map_path))
    for file in os.listdir(json_folder):
        merge_json(read_json_file(json_folder + file), ignore_ids, merged_result, ignored_result)

    write_as_json_file(merged_result_path, merged_result)
    write_as_json_file(ignored_result_path, ignored_result)
