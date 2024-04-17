import urequests

def get_date_and_time():
    url = 'http://worldtimeapi.org/api/timezone/Europe/Berlin'
    
    # GET-Anfrage an die API senden
    response = urequests.get(url)
    
    try:
        # Überprüfen, ob die Anfrage erfolgreich war
        if response.status_code == 200:
            data = response.json()
            
            # Aktuelle Zeit extrahieren
            current_time = data['datetime']
            
            # Datum und Uhrzeit extrahieren
            date_part, time_part = current_time.split('T')
            time_part = time_part.split('.')[0]  # Entfernen der Millisekunden und Zeitzone
            
            # Rückgabe von Datum und Uhrzeit als Tuple
            return date_part, time_part
        else:
            print(f"Fehler bei der Anfrage: HTTP-Statuscode {response.status_code}")
            return None, None
    finally:
        # Die Verbindung schließen
        response.close()