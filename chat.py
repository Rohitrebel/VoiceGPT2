import requests
import streamlit as st

# Title and description
st.title("🧠 Mistral Voice/Text Chatbot")
st.write("Ask me anything, and I’ll respond using Mistral-7B via OpenRouter!")

# Retrieve the API key from Streamlit secrets
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("OpenAI API key not found in Streamlit secrets. Please add it in the Secrets tab.")
    st.stop()

# Function to get response from Mistral model via OpenRouter
def get_response(user_input):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant. Keep your answers short and informative, no longer than 3-4 sentences."},
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 150
    }

    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# User input
user_input = st.text_input("Type your question here 👇", "")

if user_input:
    with st.spinner("Thinking..."):
        reply = get_response(user_input)
        st.markdown(f"**Assistant:** {reply}")

