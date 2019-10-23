from flask import Flask, request, jsonify
from flask_cors import CORS
from requests import post
import json
import os

app = Flask('__main__')
CORS(app)


@app.route('/predicciones', methods=['GET'])
def proxy_post():    
    data = _load_data()
    
    return jsonify(data)


@app.route('/')
def index():
    return "Hello"

def _load_data():
    file_dir = os.path.dirname(os.path.abspath(__file__))    
    file_route = '/prediccion.json'
    file_option = 'r'
    with open(file_dir + file_route, file_option) as f:
        config = json.load(f)
    return config

app.run(host='0.0.0.0', port=8090)

