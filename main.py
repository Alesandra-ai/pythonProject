import os

from CSVtoJSON import csv_to_json
from JSONSchemaCollision import merge_json_schemas, make_base_schema
from JsonToSchema import json_to_schema
from JsonToSchemaMapper import convert_json_file

csv_dir = 'test_data/input/csv/'
json_dir = 'test_data/input/json/'
schema_dir = 'test_data/output/temp_schema/'
merged_schema = 'test_data/output/result/schema/merged_schema.json'
json_result_folder = 'test_data/output/result/json/'


def test_run():
    for csv_file_name in os.listdir(csv_dir):
        csv_to_json(csv_dir + csv_file_name, json_dir + csv_file_name + '_out.json')

    for json_file_name in os.listdir(json_dir):
        json_to_schema(json_dir + json_file_name, schema_dir + json_file_name + '_schema.json')

    make_base_schema(merged_schema)
    for schema_file_name in os.listdir(schema_dir):
        merge_json_schemas(merged_schema, schema_dir + schema_file_name)

    for json_file_name in os.listdir(json_dir):
        convert_json_file(json_dir + json_file_name, merged_schema, json_result_folder + json_file_name + '_mapped.json')


if __name__ == '__main__':
    test_run()
