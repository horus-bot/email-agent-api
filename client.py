from groq import Groq
from config import load_api_key

def chatbot(messages, systemprompt=None):
    apikey = load_api_key()
    client = Groq(api_key=apikey)

    # Default system prompt if none provided
    if systemprompt is None:
        systemprompt = "You are a helpful assistant.your job is to gather information from the user about the network problem , you will answer in short and concise manner and after you have gathered enough information you will ask the user to raise the query and press the send email button make sure u dont ask more than 5 questions"

    # Add system prompt at the beginning
    messages.insert(0, {"role": "system", "content": systemprompt})

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
        temperature=0.7,
    )

    return completion.choices[0].message.content


def chatbot2(user_message: str, systemprompt: str = None):
    apikey = load_api_key()
    client = Groq(api_key=apikey)

    if systemprompt is None:
        systemprompt = "You are a helpful assistant.that will make a summary of the chat history and list all the important information that the user has provided related to the network problem"

    messages = [
        {"role": "system", "content": systemprompt},
        {"role": "user", "content": user_message}
    ]

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
        temperature=0.7,
    )

    return completion.choices[0].message.content
