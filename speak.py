import edge_tts

async def speak(text):
    print("Generating speech:", text)

    communicate = edge_tts.Communicate(
        text,
        voice="en-IN-PrabhatNeural"
    )

    await communicate.save("static/output.mp3")

    print("Speech generated successfully")