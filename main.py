# Voice-Activated Personal Assistant: Build a personal assistant that performs tasks like setting
# reminders, checking the weather, and reading the news. Integrate with speech recognition and
# text-to-speech libraries to create an interactive, voice-activated experience

import re
import pyttsx3
import speech_recognition as sr
import reminder
import news

r = sr.Recognizer()
r.pause_threshold = 1.2 
mic = sr.Microphone()
engine = pyttsx3.init()

def text_to_speak(command) -> str:
    try : 
        engine.say(command)
        engine.runAndWait()
    except ReferenceError as e :
        print(e)

def speak_to_text():
        
    with mic as source:
        #adjust noise
        r.adjust_for_ambient_noise(source, duration=1)

        # creates audio data
        print("Say something!")
        audio = r.listen(source)
        # converts audio data to string
        try :
            voice = r.recognize_google(audio) #text
            return voice

        except sr.UnknownValueError :
            print("Unknown value")
            return ""
        except sr.RequestError as e :
           print("Could not request results from Google Speech Recognition service")
           return ""



while True : 

    command = speak_to_text()

    print(command)

    if "reminder" in command or "set" in command : 
        #Ask reminder
        text_to_speak("Provide me reminder ?")
        reminder_V = speak_to_text() # reminder in text
        print(reminder_V)
        text_to_speak("how much time")
        var = speak_to_text()
        match = re.search(r'\d+', var)
        print(match)
        if match:
            number = int(match.group()) # time
        else:
            print("Something went wrong, Try again !")


        reminder.reminder(reminder_V, number)

    elif "news" in command :
        print("What news do you want to know")
        while True : 
            voice = speak_to_text()

            if voice and voice.split()[0] == "no":
                print("Sure !")
                break
            else :
                Enews = news.news(voice)
                print(Enews)
                print("Do you like to hear more news ? tell yes or no only !")

