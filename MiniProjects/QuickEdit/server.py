#!/usr/bin/env python
import flask
import pdb
from flask import *
app = Flask(__name__)
import os
@app.route('/')
def hello_world():
    #return 'Hello World!'
    return flask.send_from_directory('.', "index.html")

@app.route('/<path:filename>')
def send_foo(filename):
    return send_from_directory('.', filename)


# run Here
app.debug = True
app.run(host='0.0.0.0')

