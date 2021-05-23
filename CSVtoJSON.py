import csv
import json

csvFilePath = 'edu.gov_2885_27.12.2011_recommended-books.csv'
jsonFilePath = 'edu.gov_2885_27.12.2011_recommended-books_csv_out.json'

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='UTF-8') as csvFile:
        csvReader = csv.DictReader(csvFile, dialect='excel-tab')

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['index']
            data[key] = rows

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='UTF-8') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4, ensure_ascii=False))


# Call the make_json function
make_json(csvFilePath, jsonFilePath)
