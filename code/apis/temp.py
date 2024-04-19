#import Skripte
import wifi
import datetime
import calendar
import News
import weather
import gc
import toDo

print(gc.mem_free())

#WLAN Verbindung herstellen:
ssid = 'Notebook von Tobi'
password = '1357924680'
result = wifi.connect_to_wifi(ssid, password)
print("Verbindungsstatus:", result)

#Uhrzeit anzeigen
date, time = datetime.get_date_and_time()
if date and time:
    print("Datum:", date)
    print("Uhrzeit:", time)

#Kalender
url = 'http://p139-caldav.icloud.com/published/2/MTE1NzQwNjE0NzQxMTU3NDmLjpu4-S1Y9s3ZY6FOrrHnIwf0-kAOhn-6sr24tcTFaqodbcvwQ-1iUIyMWm_Q-QI6qieG29wXJSUU0hdN6JI'
events = calendar.get_next_events(url)
for event in events:
    print(f"Event: {event['summary']}, Start Time: {event['start_time']}")

#Nachrichten (URL muss API Key beinhalten)
url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=COIN,CRYPTO:BTC,FOREX:USD&time_from=20220410T0130&limit=10&apikey=7I5ZTASNKQWHN3PT'
news_titles = News.get_latest_news(url)
for title in news_titles:
    print(title)

# Wetter
api_url = "https://api.open-meteo.com/v1/forecast?latitude=49.1399&longitude=9.2205&daily=weather_code,temperature_2m_max,temperature_2m_min"
weather_forecast = weather.get_weather_forecast(api_url)
if weather_forecast:
    for day_weather in weather_forecast:
        print(f"Datum: {day_weather['date']}, Wetter: {day_weather['weather']}, Max Temp: {day_weather['max_temp']}, Min Temp: {day_weather['min_temp']}")


# ToDo-Liste
api_token = '7809ef7ce9f614f403703e7a9368e699f88e5348'
project_id = '2331941260'
tasks = toDo.toDoList(api_token, project_id)
if tasks:
    for content, due_date in tasks:
        print(f"Aufgabe: {content}, Fällig am: {due_date}")
else:
    print("Keine Aufgaben gefunden oder Fehler bei der Abfrage.")


print(gc.mem_free())