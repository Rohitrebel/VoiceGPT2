from listen import record_and_transcribe_audio
from chat import get_response
from speak import speak
import asyncio
import webbrowser, os



while True: 
    query = record_and_transcribe_audio().lower()
    if query == "none":
        print("I didn't get any query from your side!")
        continue

    print("You said:", query)

    # Specific Browser and Normal stuff Related Tasks
    if "hi" in query or "hello" in query:
        asyncio.run(speak("Hi I'm your VoiceGPT AI, how can I help you today?"))
        continue
    if "open youtube" in query: 
        asyncio.run(speak("Opening Youtube..."))
        webbrowser.open('www.youtube.com')
        continue
    if "open google" in query: 
        asyncio.run(speak("Opening Google..."))
        webbrowser.open('www.google.com')
        continue
    if "bye" in query:
        asyncio.run(speak("Bye! Take Care"))
        break 

    reply = get_response(query)

    asyncio.run(speak(reply))





