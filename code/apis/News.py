import urequests as requests
import time

# Angenommen, die API akzeptiert einen 'limit' Parameter, um die Anzahl der Ergebnisse zu begrenzen
url = 'https://www.tagesschau.de/api2/news/?regions=1&ressort=inland&limit=5'

while True:
    headers = {
        'Accept': 'application/json',
    }
    
    res = requests.get(url=url, headers=headers)
    
    if res.status_code == 200:
        try:
            data = res.json()
            news_items = data.get('news', [])[:5]
            
            for item in news_items:
                print(item.get('title', 'Kein Titel verfügbar'))

            time.sleep(10)
        except MemoryError:
            print("MemoryError: Die Antwort ist zu groß, um verarbeitet zu werden.")
    else:
        print(f'Fehler bei der Anfrage: HTTP-Statuscode {res.status_code}')
    
    res.close()
