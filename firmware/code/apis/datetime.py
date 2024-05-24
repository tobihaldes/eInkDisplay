import urequests

def get_date_and_time():
    url = 'http://worldtimeapi.org/api/timezone/Europe/Berlin'
    
    # GET-Anfrage an die API senden
    response = None
    try:
        response = urequests.get(url)
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
            error_date = "9999-99-99"
            error_time = "00:00:00"
            return error_date, error_time
        
    except OSError as e:
        print(f"Ein Netzwerkfehler ist aufgetreten: {e}")
        error_date = "9999-99-99"
        error_time = "00:00:00"
        return error_date, error_time
    
    finally:
        # Die Verbindung schließen, wenn sie geöffnet wurde
        if response is not None:
            try:
                response.close()
            except AttributeError:
                pass  # Falls response.close() fehlschlägt, nichts tun