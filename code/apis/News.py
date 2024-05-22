import urequests
import gc

def get_latest_news(url):
    """Funktion, die die 5 neuesten Nachrichten von einer API abruft und deren Titel zurückgibt."""
    gc.collect()
    
    headers = {
    'User-Agent': 'eInkDisplay'
    }
    response = urequests.get(url, headers=headers)
    print(response)
    try:
        if response.status_code == 200:
            data = response.json()  # Konvertiert die Antwort in ein Python-Diktat
            articles = data.get('articles', [])  # Holt das 'articles' Array aus der Antwort

            # Extrahiert die Titel der ersten fünf Nachrichtenartikel
            titles = [article.get('title', 'Kein Titel verfügbar') for article in articles[:6]]
            return titles
        else:
            print('Fehler bei der Anfrage:', response.status_code)
            return [None]*5
    finally:
        response.close()