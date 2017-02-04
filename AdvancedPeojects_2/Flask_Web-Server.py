from flask import Flask
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def echo_msg():
    pythonDictionary = {'name': 'Bob', 'age': 44, 'isEmployed': True}
    dictionaryToJson = json.dumps(pythonDictionary)
    return dictionaryToJson

if __name__ == '__main__':
    app.run(host='0.0.0.0')