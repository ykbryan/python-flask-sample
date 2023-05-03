#!/usr/bin/env python3
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! Demo!'


@app.route('/api/messages', methods=['GET'])
def messages():
    if (request.method == 'GET'):
        return jsonify({'message': 'Hello World!'})
    return jsonify({'message': 'You need to GET correctly!'})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
