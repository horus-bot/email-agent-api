import streamlit as st
from client import chatbot 

st.set_page_config(page_title="Simple ChatBot", page_icon="💬", layout="centered")

# Page Title
st.markdown("<h2 style='text-align:center;'>🤖 Simple ChatBot</h2>", unsafe_allow_html=True)

# CSS for a clean UI
st.markdown("""
    <style>
    .input-container {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .response-box {
        background-color: #e3e3e3;
        border-radius: 10px;
        padding: 15px;
        margin-top: 10px;
        color: #333;
        font-size: 1.1em;
    }
    </style>
""", unsafe_allow_html=True)

# Input box
with st.form("chat_form"):
    user_input = st.text_input("Ask something:", placeholder="Type your question here...")
    submitted = st.form_submit_button("Send")

# Dummy response logic
def get_bot_response(user_message):
    # Replace this with your real AI logic
    return f"🤖 Bot: {chatbot(user_message=user_message)}"

# On submit
if submitted and user_input:
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    st.write(f"🧑 You: {user_input}")
    response = get_bot_response(user_input)
    st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
