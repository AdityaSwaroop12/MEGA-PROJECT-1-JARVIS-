'''
Jarvis is a voice-activated virtual assistant designed to perform tasks such as web
browsing ,playing music and cracking interesting jokes

Libraries used :- speech_recognition, pyttsx3, webbrowser, pyjokes
'''
import speech_recognition as sr
import webbrowser #Built-in method
import pyttsx3
import musicLibrary
import pyjokes

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if("open google" in c.lower()):
        webbrowser.open("https://google.com")
    elif("open youtube" in c.lower()):
        webbrowser.open("https://youtube.com")
    elif("open linkedin" in c.lower()):
        webbrowser.open("https://linkedin.com")
    elif(c.lower().startswith("play")):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif("joke" in c.lower()):
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

if (__name__ == "__main__"):
    speak("Hello I am Jarvis.. What can I do for you")
    while True:
        r = sr.Recognizer()
        print("Recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 2, phrase_time_limit = 1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
            with sr.Microphone() as source:
                print("Jarvis Active")
                audio = r.listen(source)
            command = r.recognize_google(audio)

            processcommand(command)
        except Exception as e:
            print("Error; {0}".format(e))