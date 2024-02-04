print("hello world!")
from flask import Flask, request, jsonify
import os
import openai
from openai import OpenAI
from flask_cors import CORS, cross_origin
import qa

app = Flask(__name__)
CORS(app)

client = OpenAI()

@app.route('/')
def index():
  return 'Hello World'

@app.route('/bot', methods = ["POST"])
def test_():
  qa.run_script()
  return
  




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080) 
  print("test succesful!!")