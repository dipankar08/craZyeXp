from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '\u9AE\u9BF'.encode("utf-8")

if __name__ == '__main__':
 app.run(host='0.0.0.0')
