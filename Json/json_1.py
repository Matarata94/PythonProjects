import json

#json object to python dictionary
jsonData = '{"name": "Frank", "age": 39}'
jsonToPython = json.loads(jsonData)
print(jsonToPython)

#python dictionary to json object
pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
dictionaryToJson = json.dumps(pythonDictionary)
print(dictionaryToJson)