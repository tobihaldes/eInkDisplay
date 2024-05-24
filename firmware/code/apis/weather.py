import urequests
import gc

# Wettercode-Zuordnung basierend auf WMO-Codes
weather_code_mapping = {
    0: "Klarer Himmel",
    1: "Teilweise bewoelkt",
    2: "Bewoelkt",
    3: "Bedeckt",
    45: "Nebel",
    48: "Reifnebel",
    51: "Leichter Nieselregen",
    53: "Maeßiger Nieselregen",
    55: "Dichter Nieselregen",
    56: "Leichter gefrierender Nieselregen",
    57: "Dichter gefrierender Nieselregen",
    61: "Leichter Regen",
    63: "Maeßiger Regen",
    65: "Starker Regen",
    66: "Leichter gefrierender Regen",
    67: "Starker gefrierender Regen",
    71: "Leichter Schneefall",
    73: "Maeßiger Schneefall",
    75: "Starker Schneefall",
    77: "Schneegriesel",
    80: "Leichte Regenschauer",
    81: "Maeßige Regenschauer",
    82: "Heftige Regenschauer",
    85: "Leichte Schneeschauer",
    86: "Maeßige Schneeschauer",
    95: "Gewitter",
    96: "Gewitter mit leichtem Hagel",
    99: "Gewitter mit Hagel",
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
            forecast.append({
                    "date": "9999-99-99",
                    "weather": "Unbekannter Code",
                    "weathercode": "45",
                    "max_temp": "Unbekannt",
                    "min_temp": "Unbekannt"
                })
            return forecast
    except Exception as e:
        print(f"Error in weather API: {e}")
        forecast = []
        forecast.append({
                "date": "9999-99-99",
                "weather": "Unknown Code",
                "weathercode": "45",
                "max_temp": "Unknown",
                "min_temp": "Unknown"
            })
        return forecast
    finally:
        # Die Verbindung schließen, wenn sie geöffnet wurde
        if response is not None:
            try:
                response.close()
            except AttributeError:
                pass  # Falls response.close() fehlschlägt, nichts tun