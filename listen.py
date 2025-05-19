import speech_recognition as sr
from pydub import AudioSegment
import os

def record_and_transcribe_audio(audio_path=None):
    recognizer = sr.Recognizer()

    # Convert to PCM WAV
    if audio_path:
        converted_path = "converted.wav"
        audio = AudioSegment.from_file(audio_path)
        audio.export(converted_path, format="wav")

        with sr.AudioFile(converted_path) as source:
            audio_data = recognizer.record(source)

        os.remove(converted_path)
    else:
        with sr.Microphone() as source:
            print("Listening...")
            audio_data = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio_data, language='en-IN')
    except:
        text = "None"

    return text

