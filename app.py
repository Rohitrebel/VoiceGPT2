from flask import Flask, render_template, request, send_file, jsonify
from listen import record_and_transcribe_audio
from chat import get_response
from speak import speak
import asyncio
import os
import webbrowser

# ... other imports stay the same

@app.route('/process_audio', methods=['POST'])
def process_audio():
    audio_file = request.files['audio']
    audio_path = "user_input.webm"
    audio_file.save(audio_path)

    # Convert + Transcribe
    text = record_and_transcribe_audio(audio_path)
    print("User said:", text)

    # Process logic
    if "hi" in text.lower() or "hello" in text.lower():
        reply = "Hi I'm your VoiceGPT AI, how can I help you today?"
    elif "open youtube" in text.lower():
        webbrowser.open("https://www.youtube.com")
        reply = "Opening YouTube"
    elif "open google" in text.lower():
        webbrowser.open("https://www.google.com")
        reply = "Opening Google"
    elif text.lower() == "bye":
        reply = "Bye! Take care"
    else:
        reply = get_response(text)

    # Generate speech and save to static/output.mp3
    asyncio.run(speak(reply))

    # Return the file path as a JSON response
    return jsonify({"audio_url": "/static/output.mp3"})





