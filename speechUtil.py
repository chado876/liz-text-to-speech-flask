import pyttsx3

def synthesize(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def saveToFile():
    engine = pyttsx3.init()
    engine.save_to_file('Hello World', 'test.mp3')
    engine.runAndWait()

def synthesize_and_save_to_file(text, fileName):
    engine = pyttsx3.init()
    engine.save_to_file(text, "./output/" + fileName + '.mp3')
    # engine.save_to_file(text, clientPath + fileName + '.mp3')
    engine.runAndWait()
