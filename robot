import speech_recognition as sp
import time
import os
import pyttsx3,pywhatkit


def talk(words ):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 140)
    engine.setProperty("voice" , voices[0].id)
    engine.say(words)
    engine.runAndWait()

try:
    talk("hello")
    talk("i am flash")
    talk("who are you ")
    listener = sp.Recognizer()
    print("listen ... ")
    with sp.Microphone() as source:
        voice = listener.listen(source)
        command = listener.recognize_google(voice).lower()
        name = command.replace("i am" , "")
        talk("welcome" + name)
        print (command)
except:
    talk("Error please try again ")
    pass
talk("can i help you")



while True:
    try:
        listener = sp.Recognizer()
        print("listen ... ")
        with sp.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            print(command)
    except:
        print("Try again ")
        talk("error try again")
        pass

    if "open youtube" in command:
        talk("searching in youtube")
        results = command.replace("open youtube" , "")
        print(results)
        talk(results)
        pywhatkit.playonyt(results)
        pass


    elif "open my facebook" in command:
        talk("i will open your facebook")
        faceebook()
        pass

    elif "who creat you " or "who created you" in command:

        talk("adam alaa")
        time.sleep(3)
        pass

    elif "search google about" in command :
        search = command.replace("search google about", "")
        talk(search)
        pywhatkit.search(search)
        pass


    elif "i love you" in command:
        talk("i love you too ")
        pass
    elif "close" in command:
        break


    else:
        talk("please say something ")

    command = ""



def listener() :

    try:

        listen = sp.Recognizer()
        voice = listen.listen(sp.Microphone())
        command = listen.recognize_google(voice).lower()

    except:
        talk("try again later ")
