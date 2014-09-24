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
    pass

@app.route('/<path:filename>')
def send_foo(filename):
    return send_from_directory('./static', filename)


@app.route('/api/resolve', methods=['POST', 'GET'])
def login():
    error = None
    #pdb.set_trace()
    if request.method == 'POST':
       data = request.json['data']
       dlen = request.json['len']
       print dlen,'==>',data
       #g++ native/DrawBlock.cpp -o cmd  && ./cmd 8 2 3 4 0 3 5 7
       cmd = "g++ native/DrawBlock.cpp -o cmd  && ./cmd "
       for i in data:
         cmd +=" "+str(i)
       print 'running... :',cmd 
       os.system(cmd);

       if ( not data or not dlen):
          return "pass"
       else:
          pass
       
          #pass send cpp
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    #return render_template('login.html', error=error)
    ret={'status':'sucess','code':'200','data':'ABC'}
    return flask.jsonify(**ret)



# run Here
app.debug = True
app.run(host='0.0.0.0')

