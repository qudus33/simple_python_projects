import openai
import pyttsx3

def chat_bot(user_input):
    """This function connects to open ai and uses chat GPT"""
    open_ai_key = "Enter your openai api token" 
    response = openai.Completion.create(api_key=open_ai_key, engine="text-davinci-003", prompt=user_input, max_tokens=50)
    chat_text = response['choices'][0]['text'].strip()
    return chat_text

def text_to_speech(text):
    """This function coverts text to speech."""
    speech_engine = pyttsx3.init()
    voice = speech_engine.getProperty('voices')
    speech_engine.setProperty('voice', voice[0].id)
    speech_engine.setProperty('voice', 4)
    speech_engine.setProperty('rate', 150)
    speech_engine.setProperty('volume', 0.9)
    speech_engine.say(text)
    speech_engine.runAndWait()
    print("Done!")

print("""
        You can only ask three questions.
        Ask wisely.
""")
chances = 0

while chances < 3:
    question = input("Your question: ")
    answer = chat_bot(question)
    text_to_speech(answer)
    print(answer)
    chances = chances + 1

    

