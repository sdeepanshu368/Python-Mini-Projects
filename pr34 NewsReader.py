import requests
import json
import time
from win32com.client import Dispatch


def speak(s):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(s)


data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=enter key here")

result = data.json()
# print(result['status'])
# print(result)

news = result['articles']

speak("Welcome to News Channel")
speak("Here are the top ten news from India")
speak("So our first news is ")
for i in range(10):
    print(i+1)
    print(news[i]['title'])
    speak(news[i]['title'])
    print(news[i]['description'])
    speak(news[i]['description'])
    print("For more click ", news[i]['url'])
    if i >= 10:
        break
    time.sleep(1)
    if i == 9:
        speak("So our last news for today is ")
    else:
        speak("Moving To Our next news")

speak("Thanks for listening ! Have a nice day")
