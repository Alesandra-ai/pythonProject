import json

from genson import SchemaBuilder

example_json_input_file = 'edu.gov_2885_27.12.2011_recommended-books.json'
example_json_schema_result_file = 'Schema2.json'


# Function to extract a Intermediate (original) JSON Schema
# Takes the file paths as arguments
def makeJSONSchema(jsonInputFile, jsonSchemaOutIntermediate):
    # create dictionary
    dataSchema = {}

    # run JSON schema builder
    builder = SchemaBuilder()
    builder.add_schema({"type": "object", "properties": {}})

    with open(jsonInputFile, encoding='UTF-8') as fileJSON:
        file_content = fileJSON.read()
        builder.add_object(json.loads(file_content))
        dataSchema = builder.to_schema()

    with open(jsonSchemaOutIntermediate, 'w', encoding='UTF-8') as jsonFile:
        jsonFile.write(json.dumps(dataSchema, indent=4, ensure_ascii=False))


# Call the makeJSONSchema function
makeJSONSchema(example_json_input_file, example_json_schema_result_file)
