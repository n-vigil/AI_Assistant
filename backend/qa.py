OPEN_API_KEY = "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"

# import the OpenAI Python library for calling the OpenAI API
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", OPEN_API_KEY))

# from openai import OPENAI
# from langchain_openai import OpenAI
# import langchain
# import langchain_community
# from langchain_community.llms import OpenAI
# llm = OpenAI(openai_api_key = OPEN_API_KEY)
MODEL = "gpt-3.5-turbo"
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model= MODEL
)

# step 2: create a thread
thread = client.beta.threads.create()

# step 3: add a message to a thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)
# step 4: create a run
run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)



# first_question = True
# while True:
#     if first_question:
#         intro_text = input("\nEnter your question or type 'quit' to exit!\n")
#         first_question = False
#     else:
#         intro_text = input("\n Any more questions?\n")

#     if intro_text.lower == "quit":
#         break

#     print("QUESTION: \"%s\"" % intro_text)
#     answer = 3

#     def get_completion(prompt, model="gpt-3.5-turbo"):
#         messages = [{"role": "user", "content": prompt}]
#         response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0, # this is the degree of randomness of the model's output
#     )
#         quitreturn response.choices[0].message["content"]
#     print(answer)