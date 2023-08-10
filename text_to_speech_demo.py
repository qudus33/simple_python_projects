import pyttsx3

def text_to_speech(text):
    speech_engine = pyttsx3.init()
    voice = speech_engine.getProperty('voices')
    speech_engine.setProperty('voice', voice[1].id) # Change the value to change the voices (0 for male 1 for female)
    speech_engine.setProperty('voice', 4)
    speech_engine.setProperty('rate', 150)
    speech_engine.setProperty('volume', 0.9)
    speech_engine.say(text)
    speech_engine.runAndWait()
    print("Done!")

print("Let's play a game. I will repeat what ever you type. You have 3 chances.")
chances = 0
while chances < 3:
    value = input("Type anything: ")
    text_to_speech(value)
    chances = chances + 1


