import urequests

# URL der API
url = 'http://worldtimeapi.org/api/timezone/Europe/Berlin'

# GET-Anfrage an die API senden
response = urequests.get(url)

# Überprüfen, ob die Anfrage erfolgreich war
if response.status_code == 200:
    # Antwort in JSON-Format konvertieren
    data = response.json()
    
    # Aktuelle Zeit extrahieren
    current_time = data['datetime']
    
    # Datum und Uhrzeit extrahieren und umformatieren
    # Beispiel für current_time: "2024-04-09T15:26:02.264177+02:00"
    date, time_part = current_time.split('T')
    year, month, day = date.split('-')
    time_part = time_part.split('.')[0]  # Entfernen der Millisekunden und Zeitzone
    
    # Umformatieren in "TT.MM.JJJJ HH:MM:SS"
    formatted_time = f"{day}.{month}.{year} {time_part}"
    
    # Ausgabe der umformatierten Zeit
    print(f"Datum und Uhrzeit: {formatted_time}")
else:
    print(f"Fehler bei der Anfrage: HTTP-Statuscode {response.status_code}")

# Die Verbindung schließen
response.close()
