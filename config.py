from dotenv import load_dotenv
import os 

def load_api_key():
    load_dotenv()  # Load environment variables from .env file
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables.")
    return api_key
