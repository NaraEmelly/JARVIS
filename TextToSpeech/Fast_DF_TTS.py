import requests # pip install requests
from playsound import playsound # pip install playsound==1.2.2
import os
from typing import Union # pip install typing
import sys
import time
import threading

def generate_audio(message: str,voice : str = "Matthew"):
    url: str = f"https://api.streamelements.com/kappa/v2/speech?voice=Jarvis&text=Olá"

    headers = {'User-Agent':'Mozilla/5.0(Maciontosh;intel Mac OS X 10_15_7)AppleWebKit/537.36(KHTML,like Gecoko)Chrome/119.0.0.0 Safari/537.36'}
    
    try:
        result = requests.get(url=url, headers=headers)
        return result.content
    except:
        return None
    
def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.050)  # Adjust the sleep duration for the animation speed
    print()

def Co_speak(message: str, voice: str = "Matthew", folder: str = "", extension: str = ".mp3"):
    try:
        result_content = generate_audio(message, voice)

        if not result_content:
            print("TTS Error: Empty response")
            return

        # Detecta resposta JSON de erro
        if result_content.startswith(b"{"):
            print("TTS API Error:")
            print(result_content.decode("utf-8", errors="ignore"))
            return

        file_path = os.path.join(folder, f"{voice}{extension}")

        with open(file_path, "wb") as file:
            file.write(result_content)

        playsound(file_path)
        os.remove(file_path)

    except Exception as e:
        print("TTS Error:", e)

def speak(text):
    t1 = threading.Thread(target=Co_speak,args=(text,))
    t2 = threading.Thread(target=print_animated_message,args=(text,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


#c

import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()