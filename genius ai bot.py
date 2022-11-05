#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pirzada
#
# Created:     03/10/2022
# Copyright:   (c) pirzada 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[1].id)

engine.setProperty("voices",voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__=='__main__' :
    speak("ha ustaad plug shaat hai")

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morning")

    elif hour >=12 and hour <= 18:
        speak("good afternoon")

    speak("hi, i am genius,good to serve you")


def takecommand():
    #it will recognize speechand return in string format

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print ("listening...")
        r.pause_threshold = 1

        audio=r.listen(source)

    try:
        print("recognizing....")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said :{query}\n")

    except Exception as e :
        #print(e)
        print("wapsi bol")
        return "none"

    return query

def quit():
    return exit()







if __name__=="__main__":
    wishme()
    if 1:
        query=takecommand().lower()
    if "wikipedia" in query:
        speak("searching wikipedia..")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query, sentences=2)
        speak("according to wikipedia" + str(results))
    elif "open youtube" in query:
        webbrowser.open("youtube.com")
    elif "open google" in query:
        webbrowser.open("google.com")
    elif "play game" in query:
        import game



    elif "quit" in query :
        quit()




