from flask import Flask
import sys 
import subprocess
import random
import time
import threading
import Queue
app = Flask(__name__)

stdout_queue = Queue.Queue()

import os
def produce(item =10):
  os.system('./sample.sh')

def getData():
    for line in iter(process.stdout.readline, ''):
          stdout_queue.put(line)

@app.route('/')
def hello():
    return "Hello World!"
