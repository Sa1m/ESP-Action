from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json()
    print (req_data)
    return jsonify (req_data)

@app.route('/')
def index():
    return "<h1>Welcome to server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
