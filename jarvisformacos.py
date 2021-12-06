import pyttsx3 #pip install pyttsx3 (For Speak)
import datetime 
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui (For Screenshot)
import pyscreenshot
import psutil #pip install pustil
import pyjokes #pip install pyjokes
import operator
import json
import wolframalpha
import time
from urllib.request import urlopen
import requests
import getpass
from bs4 import BeautifulSoup
import requests
from subprocess import call
from time import gmtime, strftime
from plyer import notification
import pyowm as OWM
from rich.progress import Progress


notified=False
name=''
engine = pyttsx3.init()
engine.setProperty('rate',200)
username = str(getpass.getuser())
howtocall=''
arr=['mr','ms']


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def get_location():
    """ Function To Print GeoIP Latitude & Longitude """
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://ipinfo.io/'+my_ip+'/geo')
    geo_data = geo_request.json()
    geo = geo_data['city']
    speak("Your Ip Address is   " + my_ip)
    speak("Currently you  Are At    "+ geo)


def gender_identification():
    if(len(username)> 6):
        name = username[0:8]
        data_gender = requests.get("https://api.genderize.io/?name="+name)
        gender = data_gender.json()
        gen = gender['gender']
        if 'female' in gen:
            howtocall = arr[1]
        elif 'male' in gen:
            howtocall = arr[0]
        else:
            howtocall=''        
        return howtocall

    else:
        data_gender = requests.get("https://api.genderize.io/?name="+username)
        gender = data_gender.json()
        gen = gender['gender']
        if 'female' in gen:
            howtocall = arr[1]
        elif 'male' in gen:
            howtocall = arr[0]
        else:
            howtocall=''        
        return howtocall


def weather(city):
    owm = OWM('39150c1224ea99f8dcc8ccbd7403afd5') # PyOWM API_key
    mng = owm.weather_manager()
    obs = mng.weather_at_place(city)
    w = obs.weather
    w.reference_time(timeformat='iso')
    x = w.detailed_status # returns Atmosphere status
    y = w.humidity # returns humidity
    z = w.temperature(unit='celsius') # returns temperatutre
    print('The Atmosphere Has ' + x)
    speak('The Atmosphere Has ' + x)
    print('The Maximum Temperature For Today is %d degree celsius and the Minimum Temperature is %d degree celsius' % (z['temp_max'], z['temp_min']))
    speak('The Maximum Temperature is %d degree celsius and the Minimum Temperature is %d degree celsius' % (z['temp_max'], z['temp_min']))
    print('And The Humidity Outside is %d percentage.' % (y))
    speak('And The Humidity Outside is %d percentage.' % (y))
    if z['temp'] >= 30:
        print('The Weather Outside is Very Hot, I Suggest You Stay Home and Stay Hydrated ')
        speak('The Weather Outside is Very Hot, I Suggest You Stay Home')
    elif z['temp'] > 24 and z['temp'] < 30:
        print('The Weather Outside is Moderately Hot, I Suggest You Wear Light Cloths and a Hat to avoid Heat')
        speak('The Weather Outside is Moderately Hot, I Suggest You Wear Light Cloths and a Hat to avoid Heat')
    elif z['temp'] > 16 and z['temp'] <= 24:
        print('The Weather Outside is Warm, I Suggest You Wear Sunglasses and a Hat')
        speak('The Weather Outside is Warm, I Suggest You Wear Sunglasses and a Hat')
    elif z['temp'] < 16:
        print('The Weather Outside is Cold, I Suggest You Wear Warm Clothes')
        speak('The Weather Outside is Cold, I Suggest You Wear Warm Clothes')

    loc = mng.forecast_at_place(city,'3h')
    clouds = str(loc.will_have_clouds())
    loc = mng.forecast_at_place(city,'3h')
    clouds = str(loc.will_have_clouds())
    rain = str(loc.will_have_rain())


    if clouds == 'True':
        speak("It may have clouds in next 5 days")
    else:
        speak("It may not have clouds in next 5 days")
    if rain == 'True':
        speak("It may rain in next 5 days")
    else:
        speak("It may not rain in next 5 days")


def google_photos():
    try:
        url = "https://photos.google.com/"
        wb.open(url)
        return True
    except Exception as e:
        print(e)
        return False

def clear(): 
    os.system('clear')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S") #for 24 hour clock
    speak("the current time is")
    speak(Time)
    Time=datetime.datetime.now().strftime("%I:%M:%S") # for 12-hour clock
    speak(Time)

def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    date = str(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back  "+ getpass.getuser())
    time_()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning ")
    elif hour >=12 and hour<18:
        speak("Good Afternoon ")
    elif hour >=18 and hour <24:
        speak("Good Evening ")
    else:
        speak("Good Night ")
    speak("Jarvis at your service. Please tell me how can I help you?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source=source,duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        with Progress() as progress:
            task1 = progress.add_task("[red]Collecting...", total=50)     
        while not progress.finished:
         time.sleep(0.02)
        query = r.recognize_google(audio, language='en-US')
        print(query)
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
 
def screenshot():
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    try:
        call(["screencapture", "Screenshot" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ".jpg"])
       # img.save(desktop+str(i)+'.png')
        

    except Exception as e:
        print(e)
    
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())


def female_voice():
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[1].id)
    speak("Successfully Changed")

def male_voice():
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[4].id)
    speak("Successfully Changed")


def Introduction():
    speak("I am JARVIS 1.0 , Personal AI assistant , "
    "I am created by Ishaque  , "
    "I can help you in various regards , "
    "I can search for you on the Internet , "
    "I can also grab definitions for you from wikipedia , "
    "In layman terms , I can try to make your life a bed of roses , "
    "Where you just have to command me , and I will do it for you , ")

def make_request(url):
  response = requests.get(url)
  return response.text
  

if __name__ == '__main__':

    
    # This Function will clean any 
    # command before execution of this python file
    clear()
    #wishme()
    weather("bangaluru")
    battery = psutil.sensors_battery()
    if battery.percent < 20:
        speak("low battery: Sir. Sir!  That's the emergency alert triggered by the power dropping below 20%.")

    
    while True:

        query = TakeCommand().lower()
        # All the commands said by user will be 
        # stored here in 'query' and will be 
        # converted to lower case for easily 
        # recognition of command 

        if 'time' in query:
            time_()
        elif 'date' in query:
            date()
        elif 'how are you' in query:
            speak("I am fine, Sir Thanks for asking")
            speak("How are you Sir?")
            if 'fine' in query or "good" in query: 
                speak("It's good to know that your fine")
            else:
                speak("I hope you get well soon.")
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        
        elif 'open youtube' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            speak("Here we go to Youtube\n")
            wb.open("https://www.youtube.com/results?search_query="+Search_term)
            time.sleep(5)
        elif 'search google' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            wb.open('https://www.google.com/search?q='+Search_term)
        
        #elif 'search' in query: 
            #query = query.replace("query","")
            #wb.open(query)
        
        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")
        elif "why you came to this world" in query:
            speak("Thanks to Ishaque . further it is a secret")
        elif 'word' in query:
            speak("opening MS Word")
            word = r'Word path'
            os.startfile(word)

        elif 'what is love' and 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , "
            "And I think it is just a mere illusion , "
            "It is waste of time")

        # elif 'empty recycle bin' in query:
        #     winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
        #     speak("Recycle Bin Recycled") 

        elif 'search in chrome' in query:
            speak("What should I search ?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
            
        elif 'remember that' in query:
            speak("What should I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())
        
        
        elif "write a note" in query:
            speak("What should i write, sir")
            note = TakeCommand()
            file = open('note.txt', 'w')
            speak("Should i include date and time")
            dt = TakeCommand()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done')
            else:
                file.write(note)
                
        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read()) 

        elif "weather" in query: 

            speak(" City name ")
            print("City name : ")
            city = TakeCommand()
            city = city+" weather"
            weather(city)
            print("Have a Nice Day:)")


        elif 'female voice' in query:
            female_voice()

        elif 'male voice' in query:
            male_voice()

        elif 'covid stats' in user_query:

            html_data = make_request('https://www.worldometers.info/coronavirus/')
            # print(html_data)
            soup = BeautifulSoup(html_data, 'html.parser')
            total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
            total_cases = total_global_row.find_all('td')[2].get_text()
            new_cases = total_global_row.find_all('td')[3].get_text()
            total_recovered = total_global_row.find_all('td')[6].get_text()
            print('total cases : ', total_cases)
            print('new cases', new_cases[1:])
            print('total recovered', total_recovered)
            notification_message = f" Total cases : {total_cases}\n New cases : {new_cases[1:]}\n Total Recovered : {total_recovered}\n"
            notification.notify(
            title="COVID-19 Statistics",
            message=notification_message,
            timeout=5)    


        elif 'news' in query:
            
            try:

                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=95fc4a9b75f447ca847f4aa0b20615c1")
                data = json.load(jsonObj)
                i = 1
                
                speak('here are some top news from the times of india')
                print('''=============== TOP HEADLINES ============'''+ '\n')
                
                for item in data['articles']:
                    
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    
            except Exception as e:
                print(str(e)) 


                
        
        elif 'take screenshot' in query:
            screenshot()
            speak("Done!")    
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'tell me about yourself' and 'who are you' in query:
            Introduction()
        #show location on map
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
            
        elif "i love you" in query:
            speak("It's hard to understand, I am still trying to figure this out.")
        

        #calculation
        elif "calculate" in query:
            
            #app_id = "wolfram alpha api"
            client = wolframalpha.Client("HVRRTX-55QGKE54WG")
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer) 

        

        #General Questions
        elif "what is" in query or "who is" in query: 
            
            # Use the same API key 
            # that we have generated earlier
            client = wolframalpha.Client("HVRRTX-55QGKE54WG")
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results") 




        #sleep-time
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening commands")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)

        #quit
        elif 'offline' in query:
            speak("going Offline")
            quit()