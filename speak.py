import os
import uuid
import asyncio
import pygame
import edge_tts

async def speak(text):
    # Generate a unique filename
    filename = "output.mp3"

    # Generate the speech file
    communicate = edge_tts.Communicate(text, voice="en-IN-PrabhatNeural")
    await communicate.save(filename)

    # Initialize and play using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Wait for playback to finish
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    # Stop and clean up pygame mixer
    pygame.mixer.music.stop()
    pygame.mixer.quit()

    # Delete the file after speaking
    try:
        os.remove(filename)
    except Exception as e:
        print(f"⚠️ Could not delete {filename}: {e}")


