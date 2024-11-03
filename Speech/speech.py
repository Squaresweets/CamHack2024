import speech_recognition as sr
import pyttsx3
import asyncio
from Intelligence.intellegence import aiChat
import threading
import time


class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()

    def speakText(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def syncSpeech(self, text):
        self.speakText(text)

    def getInputText(self):
        with sr.Microphone() as source:
            #r.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.r.listen(source)
            print("Recognizing...")
            try:
                text = self.r.recognize_google(audio)
            except:
                text = "Speech not recognised"
            return text

class Listen:
    def __init__(self):
        pass

    currentState = 0 # 0: idle, 1: listening 3: Done
    lastInput = ""
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 1568
    recognizer.dynamic_energy_threshold = True

    @staticmethod
    def daemon():
        with sr.Microphone() as microphone:
            while True:
                while not Listen.currentState == 1:
                    time.sleep(0.1)
                print("Listening...")
                audio = Listen.recognizer.listen(microphone)
                print("Recognising...")
                try:
                    Listen.lastInput = Listen.recognizer.recognize_google(audio)
                    print("Recognised: " + Listen.lastInput)
                except:
                    Listen.lastInput = "Speech not recognised"
                    print("Speech not recognised")
                Listen.currentState = 2

    @staticmethod
    def start_daemon():
        recognition_thread = threading.Thread(target=Listen.daemon)
        recognition_thread.daemon = True  # This makes sure the thread will close when the main program exits
        recognition_thread.start()
