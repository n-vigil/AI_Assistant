from openai import OpenAI
OPENAI_API_KEY = "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"
client = OpenAI(api_key=OPENAI_API_KEY)


def run_script():
    OPENAI_API_KEY = "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"
    client = OpenAI(api_key = "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")

    first_question = True
    while True:
        if first_question:
            intro_text = input("\nEnter your question or type 'quit' to exit!\n")
            first_question = False
        else:
            intro_text = input("\n Any more questions?(Type 'quit' to exit)\n")

        if intro_text.lower() == "quit":
            break

    # Use the OpenAI API to generate a response with the chat model
        response = client.chat.completions.create(model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You serve as a helpful assistant, specializing in providing users with information on volunteering opportunities and food banks. Users can inquire about available volunteering positions, receive details on specific organizations, and obtain contact information. Similarly, the chatbot assists in locating nearby food banks, offering addresses and contact details. It also gives government resources to assist in food insecurity. To maintain focus, if users pose unrelated questions, the chatbot gently redirects them to its primary role of providing valuable information about volunteering opportunities and food banks. This ensures a seamless and efficient user experience centered around community engagement and assistance.  A question with no location will be followed up by the question 'What is the location that you are searching for resources' The user may answer with an address, city, or zip code."},
            {"role": "user", "content": intro_text}
        ])

        # Get the generated answer from the API response
        answer = response.choices[0].message.content.strip()

        print("ANSWER: \"%s\"\n" % answer)
run_script()
