from flask import Flask
from flask import request
from flask.json import jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json()
    print (req_data)
    return jsonify (req_data)