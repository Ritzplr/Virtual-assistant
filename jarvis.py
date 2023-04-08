import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
import subprocess
import pywhatkit
import cv2
from requests import get
import pyjokes


# text to speech kar raha.. voices bana raha

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices) 
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 200)

def speak(audio): #audio is variable that has text
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wish():
    hour= int(datetime.datetime.now().hour)
    tt= datetime.datetime.now().strftime('%I:%M %p')
    if hour >= 0 and hour<12:
        speak(f"good morning sarah. I am virtual assistant isis. Its {tt}. How may i help you")
    elif hour>=12 and hour<18:
        speak(f"good afternoon sarah. I am virtual assistant isis. Its {tt}. How may i help you")
    else:
        speak(f"good evening sarah. I am virtual assistant isis. Its {tt}. How may i help you")

#audio to text
def takecom():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio= r.listen(source)
        
    try:
        print("Recognising...")
        text= r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:
        print("Network connection error")
        return 'none'
    return text

def TaskExe():
    speak("Hello, I am Isis")
    speak("How can i help you?")

    #main func

if __name__=="__main__":
    wish()
    while True:
        query= takecom().lower()

        if "wikipedia" in query:
            speak("searching details... Wait")
            query.replace("Wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        elif "open youtube" in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")
        # elif "open google" in query or "search" in query or "who" in query or "find" in query:
        #     speak ("maam, what should i type on google")
        #     cm= takecom().lower()
        #     webbrowser.open(f"{cm}")
        elif "goodbye" in query or "sleep now" in query or "bye" in query :
            speak ("good bye. come back soon")
            exit()
        elif "what is the time" in query:
            time=datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            engine.say(time)
            engine.runAndWait()
        elif "play" in query:
            b= 'Opening youtube'
            engine.say(b)
            engine.runAndWait()
            pywhatkit.playonyt(query)
        elif "search" in query or "who" in query or "find" in query or "open google" in query:
            c= "Opening google"
            engine.say(c)
            engine.runAndWait()
            pywhatkit.search(query)
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam' , img)
                k= cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "ip address" in query:
            ip= get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")
        # elif "close youtube" in query:
        #     speak(" okay maam. closing youtube")
        #     subprocess.call("TASKKILL /F /IM Youtube.exe")
        elif "tell me a joke" in query:
            joke= pyjokes.get_joke()
            speak(joke)
        elif "close google" in query:
            speak("closing google")
            os.system("TASKKILL /F /im msedge.exe")
        elif "close youtube" in query:
            speak("closing youtube")
            os.system("TASKKILL /F /im chrome.exe")
        elif "internet speed" in query or "internet connection" in query:
            import speedtest
            st = speedtest.speedtest()
            dl= st.download()
            up= st.upload()
            speak(f"Maam we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
        elif "power" in query or "battery" in query:
            import psutil
            battery= psutil.sensors_battery()
            percentage= battery.percent
            speak(f"Maam our system have {percentage} percent battery")
        elif "take a break" in query:
            speak("okay maam.")
            break
        elif "translate" in query:
            from Translator import translategl
            query= query.replace("isis","")
            query= query.replace("translate","")
            translategl(query)
        # else:
        #     temp= query.replace(' ','+')
        #     g_url= "https://www.google.com/search?q="
        #     res_g = "sorry i cant understand but i will search this on google"
        #     print(res_g)
        #     speak(res_g)
        #     webbrowser.open(g_url+temp)

        
