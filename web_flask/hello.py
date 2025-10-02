#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, World!, my name is ibrahim and I'll get a job soon in shaa' Allah"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
