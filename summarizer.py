from client import chatbot2

def summarize_chat(messages: list[dict]) -> str:
    """
    Summarizes the entire chat history into a clean admin report.
    """

    conversation_text = ""
    for msg in messages:
        conversation_text += f"{msg['role'].capitalize()}: {msg['content']}\n"

    system_prompt = (
        "You are an expert support bot. Summarize this Wi-Fi support conversation "
        "in a short, clear report suitable for the admin. Include key complaints and any clues "
        "about the issue."
    )

    summary = chatbot2(
        user_message=conversation_text,
        systemprompt=system_prompt
    )
    return summary
