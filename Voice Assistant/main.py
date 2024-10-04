import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!") 
    else:
        speak("Good Evening Sir!") 

    assname = "voice assistant created by Hardik"
    speak("I am your Assistant")
    speak(assname)

def fetch_news(query):
    # Construct the URL for the news API
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    url = f"https://newsapi.org/v2/everything?q={query}&to={today_date}&sortBy=publishedAt&language=en&apiKey=f14c53fc782a4c2d8c78fa8f1299708a"
    
    try:
        # Make the API request
        response = requests.get(url)
        
        if response.status_code == 200:
            news = response.json()
            speak("Here are some news articles:")
            for article in news["articles"]:
                title = article.get('title', 'N/A')
                description = article.get('description', 'N/A')
                speak(f"Title: {title}")
                print(f"Title: {title}\nDescription: {description}\n")
        else:
            speak("I couldn't fetch the news at this time.")
            print(f"Failed to fetch news. Status code: {response.status_code}")
    except Exception as e:
        print(e)
        speak("An error occurred while fetching news.")

def get_weather(city_name):
    API_KEY = "5df265747d2b4bb793b42830242609"
    base_url = "http://api.weatherapi.com/v1/current.json?"
    complete_url = f"{base_url}key={API_KEY}&q={city_name}&aqi=no"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if "error" in data:
        speak("City not found.")
        print("City not found.")
    else:
        location = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        
        weather_info = (f"Location: {location}, {region}, {country}. "
                        f"Temperature: {temperature}°C. "
                        f"Condition: {condition}.")
        
        speak(weather_info)
        print(weather_info)



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5)  # Add timeout here
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")
            return "Listening timed out."
        except Exception as e:
            print(e)  # Print the exception for debugging
            return "Some Error Occurred. Sorry from Jarvis"







def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in Gmail
    server.login('email id', 'email password')
    server.sendmail('email id', to, content)
    server.close()

if __name__ == '__main__':
    
    print('Welcome to Jarvis A.I')
    speak("Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song
        if "open music" in query:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            os.system(f"open {musicPath}")

    
    
    
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to YouTube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Overflow. Happy coding!")
            webbrowser.open("stackoverflow.com") 

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "C:\\Users\\h\\Desktop\\music"
            songs = os.listdir(music_dir)
            print(songs) 
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir, the time is {strTime}")

        elif 'open chrome' in query:
            codePath = r"C:\\Program Files\\Google\\Chrome\\Application.exe"
            os.startfile(codePath)

        elif 'email to gaurav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Receiver email address"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Whom should I send?")
                to = input() 
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that you're fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me?")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Hardik.")
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif "calculate" in query: 
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text
            print("The answer is " + answer) 
            speak("The answer is " + answer) 

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "") 
            query = query.replace("play", "")		 
            webbrowser.open(query) 

        elif "who am i" in query:
            speak("If you talk, then definitely you're human.")

        elif "why you came to world" in query:
            speak("Thanks to Hardik. Further, it's a secret")

        elif 'power point presentation' in query:
            speak("Opening Power Point presentation")
            power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)

        elif 'is love' in query:
            speak("It is the 7th sense that destroys all other senses.")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Hardik")

        elif 'reason for you' in query:
            speak("I was created as a college industrial training project by Hardik.")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 
                                                       0, 
                                                       "C:\\Users\\h\\Desktop\\python proj\\wallpaper.jpg",
                                                       0)
            speak("Background changed successfully")

        elif 'open notepad' in query:
            appli = r"%windir%\system32\notepad.exe"
            os.startfile(appli)

        elif 'news' in query:
            speak("What topic do you want the news about?")
            topic = takeCommand().lower()
            fetch_news(topic)

        

        # elif 'shutdown system' in query:
        #     speak("Hold On a Sec! Your system is on its way to shut down")
        #     subprocess.call('shutdown /p /f')
            
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Emptied")

        elif "don't listen" in query or "stop listening" in query:
            speak("For how much time do you want to stop Hardik's ai from listening to commands?")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location)

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Hardik ai Camera", "img.jpg")

        # elif "restart" in query:
        #     subprocess.call(["shutdown", "/r"])
            
        # elif "hibernate" in query or "sleep" in query:
        #     speak("Hibernating")
        #     subprocess.call("shutdown /h")

        # elif "log off" in query or "sign out" in query:
        #     speak("Make sure all applications are closed before sign-out")
        #     time.sleep(5)
        #     subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should I write, sir?")
            note = takeCommand()
            file = open('hardikai.txt', 'w')
            speak("should I include date and time?")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
            file.close()
        
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r") 
            print(file.read())
            speak(file.read())

        elif "update assistant" in query:
            speak("After downloading the file, please replace this file with the downloaded one.")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)
            
            with open("Voice.py", "wb") as Pypdf:
                total_length = int(r.headers.get('content-length'))
                
                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                        expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)

        elif "heyassistant" in query:
            wishMe()
            speak("1 point o in your service, Mister/Ms")
            speak(assname)

        elif "weather" in query:
            speak("Which city's weather do you want to know?")
            city_name = takeCommand().lower()
            get_weather(city_name)
            
        # elif "send message" in query:
        #     account_sid = 'Account Sid key'
        #     auth_token = 'Auth token'
        #     client = Client(account_sid, auth_token)

        #     message = client.messages.create(
        #         body=takeCommand(),
        #         from_='Sender No',
        #         to='Receiver No'
        #     )
        #     print(message.sid)

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm " + query)
            speak("How are you, Mister?")
            speak(assname)

        elif "will you be my friend" in query: 
            speak("I'm already your friend.")

        elif "how are you" in query:
            speak("I'm fine, glad you asked.")

        elif "I love you" in query:
            speak("love is a precious human emotion, a ai chatbot cannot experience it.")

        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client("858V7Q-J789EXR525")
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")
