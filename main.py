# Voice-Activated Personal Assistant: Build a personal assistant that performs tasks like setting
# reminders, checking the weather, and reading the news. Integrate with speech recognition and
# text-to-speech libraries to create an interactive, voice-activated experience

import re
import pyttsx3
import speech_recognition as sr
import reminder
import news
import weather


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


try : 
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
                reminder.set_reminder(reminder_V, number)
            else:
                print("Something went wrong, Try again !")



        elif "news" in command :
            while True : 
                print("What news do you want to know")
                voice = speak_to_text()

                if voice and voice.split()[0] == "no":
                    print("Sure !")
                    break
                else :
                    Enews = news.news(voice)
                    print(Enews)
                    print("Do you like to hear more news ? if yes than tell directly else tell no !")

        elif "weather" in command :
            while True : 
                print("Which location ? specify only location name")
                location = speak_to_text()

                if len(location.split()) == 2 or len(location.split()) == 1 :
                    weather_condition = weather.weather(location)
                    print(weather_condition)
                    print("Do you like to check more location than tell only location name else say no !")
                elif location and location.split()[0] == "no" :
                    print("Sure !")
                    break
                else : 
                    print("Input is not processable, Try again !")
        elif command and command.split()[0] == "no" :
            print("See you again !")
            break
except KeyboardInterrupt as e :
    print("Thank you for using this service see you soon !")
              
