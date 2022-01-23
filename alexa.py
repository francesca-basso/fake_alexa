import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import mpyg321
import requests, json
import webbrowser
import playsound

def respond(audioString):
	print(audioString)
	tts = gTTS(text=audioString, lang='en')
	tts.save("speech.mp3")
	playsound.playsound("speech.mp3")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data

def digital_assistant(data):
    global listening
    if "how are you" in data:
        listening = True
        respond("I am well")

    if "what time is it" in data:
        listening = True
        respond(ctime())
        
    if "stop listening" in data:
        listening = False
        respond("Glad to be of servie")

    if "where is" in data:
        listening = True
        data = data.split(" ")
        location_url = "https://www.google.com/maps/place/" + str(data[2])
        respond("Hold on Francesca, I will show you where " + data[2] + " is.")
        webbrowser.open(location_url)

    return listening


time.sleep(1)
respond("Hi Francesca, what can I do for you?")
listening = True
while listening == True:
    data = listen()
    listening = digital_assistant(data)
if listening == False:
	os.remove("speech.mp3")
