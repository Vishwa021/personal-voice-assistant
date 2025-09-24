# Voice-Activated Personal Assistant: Build a personal assistant that performs tasks like setting
# reminders, checking the weather, and reading the news. Integrate with speech recognition and
# text-to-speech libraries to create an interactive, voice-activated experience

import pyttsx3
import speech_recognition as sr
import reminder

r = sr.Recognizer()
r.pause_threshold = 1.2 
mic = sr.Microphone()

def text_to_speak(command) -> str:
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def speak_to_text():

    with mic as source : 
        r.adjust_for_ambient_noise(source, duration=1)
        
    



    try :
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=1)
            while True:    
                # creates audio data
                print("🎤 Listening for commands... (press Ctrl+C to stop)")
                print("Say something!")
                audio = r.listen(source)
                # converts audio data to string
                try :
                    voice = r.recognize_google(audio) #text
                    
                except sr.UnknownValueError :
                    text_to_speak("I didn't understand.")

                except sr.RequestError as e :
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))

                if "reminder" in voice or "set" in voice : 
                    #Ask reminder
                    text_to_speak("what is your reminder ?")

                    reminder.reminder()

    except KeyboardInterrupt:
        print("\n👋 Exiting on user request.")





















