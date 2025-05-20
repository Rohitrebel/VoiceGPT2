🎙️ VoiceGPT2
VoiceGPT2 is a Python-based voice assistant that integrates speech recognition, text-to-speech synthesis, and conversational AI to provide an interactive voice interface. It captures user speech, processes it through a conversational model, and responds audibly, creating a seamless voice-driven experience.

🚀 Features
Speech Recognition: Converts spoken words into text using audio input.

Conversational AI: Processes user input through a chat model to generate meaningful responses.

Text-to-Speech: Transforms AI-generated text responses back into speech for audible interaction.

Web Interface: Offers a user-friendly web interface for interaction.

🛠️ Technologies Used
Python: Core programming language.

Flask: Web framework for handling HTTP requests and rendering templates.

SpeechRecognition: Library for performing speech recognition.

gTTS (Google Text-to-Speech): Converts text to speech.

PyDub: Handles audio file manipulation.

HTML/CSS: Frontend structure and styling.

📁 Project Structure
php
Copy
Edit
VoiceGPT2/
├── app.py               # Main Flask application
├── chat.py              # Handles chat model interactions
├── listen.py            # Captures and processes audio input
├── speak.py             # Converts text responses to speech
├── templates/
│   └── index.html       # Web interface template
├── static/
│   └── styles.css       # Styling for the web interface
├── requirements.txt     # Python dependencies
└── .gitignore           # Specifies files to ignore in Git


🎯 Usage
Click the "Start" button on the web interface.

After Speaking out your query click on "Stop" button when you are finished speaking.

Your speech will be transcribed and processed.

The AI model generates a response, which is then converted to speech and played back to you.
