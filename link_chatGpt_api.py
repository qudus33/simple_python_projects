import openai

user_input = "Hello world!"

open_ai_key = "Enter your api token"    # Check your openai account.

response = openai.Completion.create(api_key=open_ai_key, engine="text-davinci-003", prompt=user_input, max_tokens=50)   # Chat engine model can be changed. Token can also be changes.

print(response)     #print("ChatGPT: ", response)

chat_text = response['choices'][0]['text'].strip()  # Extract the text data from the response

print(chat_text)

