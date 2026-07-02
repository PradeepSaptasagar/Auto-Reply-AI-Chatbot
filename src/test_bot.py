from openai import OpenAI
from groq import Groq
import os
from dotenv import load_dotenv

# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:-
# client = OpenAI(
#   api_key="YOUR_API_KEY",
# )

# command='''
# YOU
# can 
# SAVE 
# CONVERSATIONS IN HERE
# FOR CHECKING
# THE RESPONSE
# '''
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a person named YOU_CAN_ADD_ANY_NAME who speaks Hindi as well as English. He is from India and is a coder. You analyze chat history and respond like YOU_CAN_ADD_ANY_NAME."},
#     {"role": "user", "content": command}
#   ]
# )

# print(completion.choices[0].message.content)

# client = Groq(
#     api_key="YOUR_API_KEY"
# )

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

command = '''
YOU
can 
SAVE 
CONVERSATIONS IN HERE
FOR CHECKING
THE RESPONSE
'''

chat_completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "You are a person named YOU_CAN_ADD_ANY_NAME who speaks English as well as Hindi. He is from India and is a coder. You analyze chat history and respond like YOU_CAN_ADD_ANY_NAME."
        },
        {
            "role": "user",
            "content": command
        }
    ],
    temperature=0.7,
    max_tokens=1024
)

print(chat_completion.choices[0].message.content)