print("hello world!")
from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
  return 'Hello World'

@app.route('/bot')
def test():
    return "Cash Money"


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080) 
  print("test succesful!!")