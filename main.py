#Modules imported
import speech_recognition as sr
import setuptools
from random import choice
from conv import finetext
from conv import goodbye
import webbrowser
import pyttsx3
import datetime
from decouple import config
import os
import subprocess as sp
from online import youtube, search_on_google, search_on_wiki, get_news,weather_forecast
#import chat as ai

#User Name and Bot Name
User= config('USER')
Hostname= config('BOT')

#Setting up speech and its properties
engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 4)
engine.setProperty('rate', 220)
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Speaking function
def speak(text):
    engine.say(text)
    engine.runAndWait()   

#greeting function
def greet_me():
    hour= datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak(f"Good morning!Ma'am {User}")
        print(f"Good morning!Ma'am {User}")
    elif 12 <= hour < 17:
        speak(f"Good afternoon!Ma'am {User}")
        print(f"Good afternoon!Ma'am {User}")
    elif 17 <= hour < 20:
        speak(f"Good evening!Ma'am {User}")   
        print(f"Good evening!Ma'am {User}")     
    speak(f"Hello! I am {Hostname}. How may I assist you?")     
    print(f"Hello! I am {Hostname}. How may I assist you?")     

#processing the command   
def processcommand(c):
    print(c)
    #open sites
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"], ["instagram", "https://www.instagram.com"]]
    for site in sites:
        if c.lower()==f"Open {site[0]}".lower():
            speak(f"Opening {site[0]}")
            webbrowser.open(site[1])
    #tell the time
    if "the time" in c.lower():
        time= datetime.datetime.now().strftime("%H:%M")
        speak(f"the time is {time}")
    #tell the date    
    elif "the date" in c.lower():
        day= datetime.datetime.now().strftime("%d")
        month= datetime.datetime.now().strftime("%m")
        year= datetime.datetime.now().strftime("%Y")
        speak(f"Today is {day} {month} of year {year}") 
    #open command prompt
    elif "open command prompt" in c.lower():
        try:
            speak("Opening command Prompt")
            os.system('start cmd')
        except Exception as e:
            print(f"Error: {e}")
    #Open Camera        
    elif "open camera" in c.lower():
        speak("Opening Camera")
        sp.run('start microsoft.windows.camera:', shell=True)
    #Open Notepad    
    elif "open notepad" in c.lower():
        speak("Opening Notepad")
        notepad_path= "C:\\Windows\\system32\\notepad.exe"
        os.startfile(notepad_path)
    #Open Microsoft Word    
    elif "open microsoft word" in c.lower():
        speak("Opening Microsoft word")
        word_path= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk"                    
        os.startfile(word_path) 
    #Search on Youtube    
    elif "search on youtube" in c.lower(): 
        speak("What do you want me to play?Ma'am")
        search_term = takecommand()  # Wait for user input
        if search_term:
            speak(f"Searching {search_term} on Youtube")
            youtube(search_term)
    #Search on Google         
    elif "search on google" in c.lower():
        speak("What do you want me to search?Ma'am")
        query=takecommand()  # Wait for user input
        if query:
            speak(f"Searching {query} on Google")
            search_on_google(query)
    #Search on Wikipedia        
    elif "search on wikipedia" in c.lower():
        speak("What do you want me to search?")
        search = takecommand()
        results = search_on_wiki(search)
        speak(f"According to wikipedia,{results}")
        speak("I am printing in on terminal")
        print(results)
    #Tell the Headlines
    elif "tell me news" in c.lower():
        speak(f"I am reading out the latest headline of today,Ma'am")
        news_headlines = get_news()
        for headline in news_headlines:
            speak(headline)
        speak("I am printing it on screen,Ma'am")
        print(*get_news(), sep='\n')
    elif 'weather' in c.lower():
        city = "multan"
        speak(f"Getting weather report for your city {city}")
        weather, temp, feels_like = weather_forecast(city)
        speak(f"The current temperature is {temp}, but it feels like {feels_like}")
        speak(f"Also, the weather report talks about {weather}")
        speak("For your convenience, I am printing it on the screen ma'am.")
        print(f"Description: {weather}\nTemperature: {temp}\nFeels like: {feels_like}")
    elif "repeat after me" in c.lower():
        speak("Okay")
        repeat= takecommand()
        speak(repeat)
'''    
    elif "chat" in c.lower():
        try:
            speak("AI is handling this request")
            print("Generating response...")
            response = ai.generate_response(c)
            print(f"AI Response: {response}")
            speak(response)
        except Exception as e:
            print(f"Error generating response: {e}")
            speak("I'm sorry, I couldn't process that request.") 
'''  



#taking command 
def takecommand():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening")
            r.pause_threshold=1
            audio = r.listen(source) 
            print("Recongnizing")
        command= r.recognize_google(audio, language='en-in')
        return command.lower()
    except Exception as e:
        print(f"Error:{e}")
        speak("Jarvis couldn't understand it.")
        return None
    


    
#RUNNING OF THE JARVIS    
if (__name__== "__main__"):
    greet_me()

    while True:
        command= takecommand()
        if (command== "jarvis"):
            speak("Yes?") 
            print("Yes?")       
        elif "how are you" in command:
            speak(choice(finetext))
        elif ("stop" or "bye" or "exit") in command:
            speak(choice(goodbye))
            exit()
        else: 
            print("Jarvis active...")
            processcommand(command)