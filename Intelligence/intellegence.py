import google.generativeai as genai
import os
import time
import traceback
genai.configure(api_key="AIzaSyCL9ZFKKtzpZNTnSZPP6sinhBm6qhLLyv4")


class aiChat:
    def __init__(self):
        pass

    model = genai.GenerativeModel("gemini-1.5-flash")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "aiPrompt.txt")
    currentChat = None

    with open(file_path, 'r') as file:
        prompt = file.read()

    @staticmethod
    def new_chat():
        aiChat.currentChat = aiChat.model.start_chat(
            history=[
                {"role": "user", "parts": aiChat.prompt},
                # {"role": "model", "parts": "Hello user, how are you today?"},
            ]
        )
    @staticmethod
    def send_message(msg):
        while True:
            try:
                print("Trying to get response to: " + msg)
                response = aiChat.currentChat.send_message(msg).text
                print("New response: " + response)
                return response
            except:
                time.sleep(0.2)