import json

#encoded a Python object (mata) into JSON.
class Employee(object):
    def __init__(self, name):
        self.name = name

def jsonDefault(object):
    return object.__dict__

mata = Employee('Mostafa')
jsonMata = json.dumps(mata, default=jsonDefault)
print(jsonMata)