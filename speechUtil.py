import pyttsx3

def synthesize(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

