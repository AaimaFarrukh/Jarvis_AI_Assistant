import wikipedia
import requests
import pywhatkit as kit
from decouple import config

news_api=config('NEWS_API')

def youtube(video):
    kit.playonyt(video)
def search_on_wiki(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        return results
    except wikipedia.exceptions.PageError:
        return f"Sorry, I couldn't find any information on '{query}' on Wikipedia."
def search_on_google(query):
    kit.search(query)  
def get_news():
    news_headline = []
    result = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}").json()
    articles = result["articles"]
    for article in articles:
        news_headline.append(article["title"])
    return news_headline[:6]
def weather_forecast(city):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e122282dabfd9092ab2563feba3bae3e").json()
    if 'weather' in res and len(res['weather']) > 0:
        weather = res["weather"][0]["main"]
        temp_kelvin = res["main"]["temp"]
        feels_like_kelvin = res["main"]["feels_like"]
            
        # Convert temperatures from Kelvin to Celsius
        temp = temp_kelvin - 273.15
        feels_like = feels_like_kelvin - 273.15
            
        return weather, f"{temp:.2f}°C", f"{feels_like:.2f}°C"
    else:
        raise KeyError("Weather information not found in API response")
