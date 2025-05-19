import speech_recognition as sr



def record_and_transcribe_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1 # Wait for 1 sec before considering the end of a phrase
        audio = r.listen(source)
    try: 
        print('Recognizing Text...')
        query = r.recognize_google(audio, language = 'en-in')
    except Exception as e:
        print("Could you say that again...")
        return "None"
    return query
