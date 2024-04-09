import urequests

# Wettercode-Zuordnung basierend auf WMO-Codes (vereinfachte und exemplarische Liste)
weather_code_mapping = {
    0: "Klarer Himmel",
    1: "Teilweise bewölkt",
    2: "Bewölkt",
    3: "Bedeckt",
    45: "Nebel",
    48: "Reifnebel",
    51: "Leichter Nieselregen",
    53: "Mäßiger Nieselregen",
    55: "Dichter Nieselregen",
    56: "Leichter gefrierender Nieselregen",
    57: "Dichter gefrierender Nieselregen",
    61: "Leichter Regen",
    63: "Mäßiger Regen",
    65: "Starker Regen",
    66: "Leichter gefrierender Regen",
    67: "Starker gefrierender Regen",
    71: "Leichter Schneefall",
    73: "Mäßiger Schneefall",
    75: "Starker Schneefall",
    77: "Schneegriesel",
    80: "Leichte Regenschauer",
    81: "Mäßige Regenschauer",
    82: "Heftige Regenschauer",
    85: "Leichte Schneeschauer",
    86: "Mäßige Schneeschauer",
    95: "Gewitter",
    99: "Gewitter mit Hagel",
}

api_url = "https://api.open-meteo.com/v1/forecast?latitude=49.1399&longitude=9.2205&daily=weather_code,temperature_2m_max,temperature_2m_min"

try:
    response = urequests.get(api_url)
    if response.status_code == 200:
        json_data = response.json()
        daily_data = json_data["daily"]

        for i in range(len(daily_data["time"])):
            date = daily_data["time"][i]
            weather_code = daily_data["weather_code"][i]
            weather_description = weather_code_mapping.get(weather_code, "Unbekannter Wettercode")
            max_temp = daily_data["temperature_2m_max"][i]
            min_temp = daily_data["temperature_2m_min"][i]
            print(f"Datum: {date}, Wetter: {weather_description}, Max Temp: {max_temp}°C, Min Temp: {min_temp}°C")

        response.close()
    else:
        print(f"Fehler beim Abrufen der Daten von der API: Statuscode {response.status_code}")
        response.close()

except Exception as err:
    print(f"Fehler beim Abrufen der Daten von der API: {err}")
