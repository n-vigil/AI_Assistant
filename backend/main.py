from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY


@app.route('/')
def index():
  return 'Hello World'

@app.route('/bot', methods=['POST'])
def ask_ai():
    data = request.get_json()

    if 'question' not in data:
        return jsonify({'error': 'Missing question parameter'}), 400

    question = data['question']

    # Use the OpenAI API to generate a response with the chat model
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "You serve as a helpful assistant, specializing in providing users with information on volunteering opportunities and food banks. Users can inquire about available volunteering positions, receive details on specific organizations, and obtain contact information. Similarly, the chatbot assists in locating nearby food banks, offering addresses and contact details. It also gives government resources to assist in food insecurity. To maintain focus, if users pose unrelated questions, the chatbot gently redirects them to its primary role of providing valuable information about volunteering opportunities and food banks. This ensures a seamless and efficient user experience centered around community engagement and assistance.  A question with no location will be followed up by the question 'What is the location that you are searching for resources' The user may answer with an address, city, or zip code."},
                {"role": "user", "content": question}
            ]
    )

    # Get the generated answer from the API response
    answer = response['choices'][0]['message']['content'].strip()

    return jsonify({'answer': answer})



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080) 
  print("test succesful!!")