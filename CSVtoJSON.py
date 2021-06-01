import csv

from JsonUtils import json_to_string

test_csv_file_name = 'data_c1.csv'
test_csv_file_path = 'test_data/input/' + test_csv_file_name
test_output_file_path = 'test_data/output/' + test_csv_file_name + '_out.json'


# Convert csv to json array
def csv_to_json(csv_file_path, output_file_path):
    with open(csv_file_path, encoding='UTF-8') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, dialect='excel-tab')
        # mapped_csv_data = map_csv(csv_dict_reader)
        mapped_csv_data = []
        for row in csv_dict_reader:
            map_function(mapped_csv_data.append, row)
        result_json_data = json_to_string(mapped_csv_data)

    with open(output_file_path, 'w', encoding='UTF-8') as output_file:
        for part in result_json_data:
            reduce_function(output_file.write, part)


def map_function(fn, part):
    fn(part)


def reduce_function(function, part):
    function(part)


csv_to_json(test_csv_file_path, test_output_file_path)
