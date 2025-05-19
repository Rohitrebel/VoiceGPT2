import os
import uuid
import edge_tts

async def speak(text):
    # Save to a consistent file name so the frontend can fetch it
    filename = "static/output.mp3"  # Ensure 'static/' folder exists and is exposed

    # Generate the speech file using Edge TTS
    communicate = edge_tts.Communicate(text, voice="en-IN-PrabhatNeural")
    await communicate.save(filename)

    # No playback here — frontend will play 'static/output.mp3'
    return filename


