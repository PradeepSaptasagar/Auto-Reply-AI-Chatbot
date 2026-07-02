import pyautogui
import time
import pyperclip
from groq import Groq
import os
from dotenv import load_dotenv

# client = Groq(
#     api_key="YOUR_API_KEY"
# )

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def is_last_message_from_sender(chat_log, sender_name="YOUR_FRIENDS_NAME"):
    # Split the chat log into individual messages
    messages=chat_log.strip().split("/ENDING_CHARACTER")[-1]
    if sender_name in messages:
        return True
    return False
    
# This project currently uses hardcoded screen coordinates for desktop automation. You may need to adjust the coordinates in whatsapp_bot.py to match your screen resolution and WhatsApp window layout.    

pyautogui.click(1239, 1043)
time.sleep(2) # Wait for 1 second to ensure the click is registered

while True:

    # Drag the mouse from the coordinates specified to select the text
    pyautogui.moveTo(674, 189)
    pyautogui.dragTo(1881, 940, duration=1.0,button='left')

    # Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl','c')
    time.sleep(2)
    pyautogui.click(1743, 360)

    # Retrieve the text from the clipboard and store it in the variable 
    chat_history=pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)

    if is_last_message_from_sender(chat_history):

        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """
                                You are YOU_CAN_ADD_ANY_NAME.

                                You are replying to WhatsApp messages as a real human.

                                You will receive the complete chat history.

                                Your job is to write ONLY the next WhatsApp message.

                                Rules:
                                - Reply naturally.
                                - Infer the intent from the latest messages instead of asking unnecessary questions.
                                - If someone shares multiple job links, assume they want you to review or apply to them.
                                - Do not ask for clarification unless the message is genuinely ambiguous.
                                - Keep the reply under 2 sentences.
                                - Reply only in English.
                                - Never mention that you analyzed the chat.
                                - Never include timestamps, names, or labels.
                                - Output only the message.
                                """
                },
                {
                    "role": "user",
                    "content": chat_history
                }
            ],
            temperature=0.7,
            max_tokens=1024
        )

        response = chat_completion.choices[0].message.content

        print(response)

        pyperclip.copy(response)

        pyautogui.click(1426, 975)
        time.sleep(2)

        pyautogui.hotkey('ctrl','v')
        time.sleep(2)

        pyautogui.press('enter')