from groq import Groq
from config import load_api_key

def chatbot(messages, systemprompt=None):
    apikey = load_api_key()
    client = Groq(api_key=apikey)

    # Optional: add system prompt at the beginning if needed
    if systemprompt:
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

    messages = []

    if systemprompt:
        messages.append({"role": "system", "content": systemprompt})

    messages.append({"role": "user", "content": user_message})

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
        temperature=0.7,
    )

    return completion.choices[0].message.content
