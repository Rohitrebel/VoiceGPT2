import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access OpenAI key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Optional: raise error if key is missing
if OPENAI_API_KEY is None:
    raise ValueError("OpenAI API key not found in .env file")


def get_response(user_input):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json", "HTTP-Referer": "http://localhost:5000",
    "X-Title": "VoiceGPT"}

    body = {
        "model": "mistralai/mistral-small-3.2-24b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant. Keep your answers short and informative, no longer than 3-4 sentences"},
            {"role": "user", "content": user_input}
        ],
        
    }

    try:
        resp = requests.post(url, headers=headers, json=body, timeout=80)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"LLM call failed: {e}"
