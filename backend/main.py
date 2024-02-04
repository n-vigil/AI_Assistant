print("hello world!")
# from openai import OPENAI
from flask import Flask
import os

# client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "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"))



app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello World'

  # Example OpenAI Python library request
# MODEL = "gpt-3.5-turbo"
# response = client.chat.completions.create(
#     model=MODEL,
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Knock knock."},
#         {"role": "assistant", "content": "Who's there?"},
#         {"role": "user", "content": "Orange."},
#     ],
#     temperature=0,
# )


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080) 
  print("test succesful!!")