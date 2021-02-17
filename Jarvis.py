import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)


searching=['can you tell me something about','can i get information about','can you tell me about','what is','who is']




def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        speak('Good Morning!')
    elif (hour>=12 and hour<18):
        speak('Good Afternoon')
    else:
        speak("Good Evening")
    speak("Password please")
    speak("If you are a guest then enter anything")
    Password=int(input())
    if (Password==42001):
        speak("Hey Boss!")
        speak("Let's begin")
    else:
        speak("Hey....... I am Jarvis created by CodeFlare")
        speak("Can I know your name")
        name=takeCommand()
        print(name)
        speak("Hello..."+str(name)+"....Welcome to the world of Artificial Intelligence")
        speak("How can i help you!")


    


def takeCommand():
#     Takes microphone input from user and gives string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=2
        # Add somemore types and try different things
        audio=r.listen(source)

    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        # print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Please say that again.....")
        return "None"
    return query


def wiki(a):
    speak('Searching...')
    results=wikipedia.summary(a,sentences=2)
    speak("According to wikipedia...")
    speak(results)




if __name__=="__main__":
    wishMe()
    f=0
    a=takeCommand().lower()
    while ('quit' not in a):
        # Conditions
        for value in searching:
            if value in a:
                a=a.replace(value,"")
                wiki(a)
                f=1
            else:
                continue
        if 'open google' in a:
            speak('launching')
            path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(path).open("google.com")
        elif 'open youtube' in a:
            speak('launching')
            webbrowser.open("youtube.com")
        elif 'play music' in a:
            music_dir='D:\\Om\\Songs'
            songs=os.listdir(music_dir)
            r=random.randint(0,2)
            speak('Playing'+str(songs[r]))
            os.startfile(os.path.join(music_dir,songs[r]))
        elif f==0:
            speak("....Sorry this is currently out of my scope....I will add new features soon....")
        a=takeCommand().lower()
    speak('Shutting down')
