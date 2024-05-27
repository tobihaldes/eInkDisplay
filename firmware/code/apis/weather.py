import urequests
import gc

# Wettercode-Zuordnung basierend auf WMO-Codes
weather_code_mapping = {
    0: "Clear sky",
    1: "Partly cloudy",
    2: "Cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Light snowfall",
    73: "Moderate snowfall",
    75: "Heavy snowfall",
    77: "Snow grains",
    80: "Light rain showers",
    81: "Moderate rain showers",
    82: "Heavy rain showers",
    85: "Light snow showers",
    86: "Moderate snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with light hail",
    99: "Thunderstorm with hail",
}

def get_weather_forecast(latitude, longitude):
    """Holt die Wettervorhersage und gibt die Details für die naechsten Tage zurück."""
    gc.collect()
    
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weather_code,temperature_2m_max,temperature_2m_min"
    
    response = None
    
    try:
        response = urequests.get(api_url)
        print(response)
        if response.status_code == 200:
            json_data = response.json()
            daily_data = json_data["daily"]
            forecast = []

            for i in range(len(daily_data["time"])):
                date = daily_data["time"][i]
                weather_code = daily_data["weather_code"][i]
                weather_description = weather_code_mapping.get(weather_code, "Unbekannter Wettercode")
                max_temp = daily_data["temperature_2m_max"][i]
                min_temp = daily_data["temperature_2m_min"][i]
                forecast.append({
                    "date": date,
                    "weather": weather_description,
                    "weathercode": weather_code,
                    "max_temp": f"{max_temp} C",
                    "min_temp": f"{min_temp} C"
                })
            
            return forecast
        else:
            print(f"Fehler beim Abrufen der Daten von der API: Statuscode {response.status_code}")
            forecast = []

            # Definiere den Inhalt, der hinzugefügt werden soll
            content = {
                "date": "9999-99-99",
                "weather": "No Data",
                "weathercode": 45,
                "max_temp": "Unknown",
                "min_temp": "Unknown"
            }

            # Füge den Inhalt siebenmal zur Liste hinzu
            for _ in range(7):
                forecast.append(content.copy())
            return forecast
    except Exception as e:
        print(f"Error in weather API: {e}")
        forecast = []

        # Definiere den Inhalt, der hinzugefügt werden soll
        content = {
            "date": "9999-99-99",
            "weather": "No Data",
            "weathercode": 45,
            "max_temp": "Unknown",
            "min_temp": "Unknown"
        }

        # Füge den Inhalt siebenmal zur Liste hinzu
        for _ in range(7):
            forecast.append(content.copy())
        return forecast
    finally:
        # Die Verbindung schließen, wenn sie geöffnet wurde
        if response is not None:
            try:
                response.close()
            except AttributeError:
                pass  # Falls response.close() fehlschlägt, nichts tun