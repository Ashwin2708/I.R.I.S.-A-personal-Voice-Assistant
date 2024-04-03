# pip install pyttsx3

import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    voices = engine.getProperty('voices')
    engine.setProperty('rate', rate-70)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

