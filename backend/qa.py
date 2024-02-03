OPEN_API_KEY = "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"

import langchain
from langchain.llms import OpenAI
llm = OpenAI(openai_api_key = OPEN_API_KEY)

first_question = True
while True:
    if first_question:
        intro_text = input("\nEnter your question or type 'quit' to exit!")
        first_question = False
    else:
        intro_text = input("\n Any more questions?")
    if intro_text.lower == 'quit':
        break