from flask import Flask, request, jsonify
from flask_cors import CORS
from requests import post
import json
import ast

app = Flask('__main__')
CORS(app)

mlflow_endpoint = 'http://mlflow-deploy:1234/invocations'

@app.route('/invocations', methods=['POST'])
def proxy_post():    
    data = json.dumps(request.json)    
    headers = {
    'Content-Type': "application/json"
    }
    response = post(url=mlflow_endpoint, data = data, headers = headers)
    return jsonify(ast.literal_eval(response.text))

@app.route('/')
def index():
    return "Hello"

app.run(host='0.0.0.0', port=8090)

