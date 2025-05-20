import requests
import os
from dotenv import load_dotenv
import streamlit as st



# Access OpenAI key
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# Optional: raise error if key is missing
if OPENAI_API_KEY is None:
    raise ValueError("OpenAI API key not found in .env file")


def get_response(user_input):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer {}".format(OPENAI_API_KEY),
        "Content-Type": "application/json"
    }

    body = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant. Keep your answers short and informative, no longer than 3-4 sentences"},
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 150 
    }

    response = requests.post(url, headers=headers, json=body)
    return response.json()["choices"][0]["message"]["content"]
