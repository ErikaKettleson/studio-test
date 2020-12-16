from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/sub_response', methods=['POST'])
def response_from_ivr():
    print(request.json())
    return 'got response'