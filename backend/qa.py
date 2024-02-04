OPEN_API_KEY = "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"

import langchain
import langchain_community
from langchain_community.llms import OpenAI
llm = OpenAI(openai_api_key = OPEN_API_KEY)

first_question = True
while True:
    if first_question:
        intro_text = input("\nEnter your question or type 'quit' to exit!\n")
        first_question = False
    else:
        intro_text = input("\n Any more questions?\n")

    if intro_text.lower == "quit":
        break

    print("QUESTION: \"%s\"" % intro_text)