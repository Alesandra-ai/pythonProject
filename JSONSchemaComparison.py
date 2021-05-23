import json

inputSchema = 'Schema1.json'
inputSchemaBase = 'Schema2.json'
SchemaOut = 'SchemaOut.json'

indexArray = ['id', 'index', 'indx']


def schemaCompare(inputSchemaIn, inputSchemaBase, SchemaOut):
    dataSchemaDict = {}
    dataSchemaBaseDict = {}
    dataSchemaOut = {}

    # Schema1 = SchemaBuilder()
    with open(inputSchemaIn, encoding='UTF-8') as file1JSONSchema:
        jsonSchemaInContent = file1JSONSchema.read()
        dataSchemaDict = json.loads(jsonSchemaInContent)

    with open(inputSchemaBase, encoding='UTF-8') as file2JSONSchema:
        jsonSchemaBaseContent = file2JSONSchema.read()
        dataSchemaBaseDict = json.loads(jsonSchemaBaseContent)

    allKeysResult = getArrayWithIndex(dataSchemaDict)
    #print(allKeysResult)

    dataSchemaOut = dataSchemaBaseDict

    for key in dataSchemaOut:
        if key not in allKeysResult:
            dataSchemaOut.update(key, ': "String"')

    with open(SchemaOut, 'w', encoding='UTF-8') as jsonFile:
        jsonFile.write(json.dumps(dataSchemaOut, indent=4, ensure_ascii=False))


def getArrayWithIndex(InputDict):
    allKeys = []

    for key in InputDict:
        if key in indexArray:
            allKeys.extend(InputDict.keys())
        elif type(InputDict.get(key)) is dict:
            allKeys.extend(getArrayWithIndex(InputDict[key]))

    return set(allKeys)


schemaCompare(inputSchema, inputSchemaBase, SchemaOut)
