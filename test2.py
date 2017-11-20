import json

def main():
    # jsonData = '{"name": "Frank", "age": 39}'
    # jsonToPython = json.loads(jsonData)
    # print jsonToPython['name']
    pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
    dictionaryToJson = json.dumps(pythonDictionary)
    print(dictionaryToJson)

main()
