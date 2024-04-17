import urequests

def get_latest_news(url):
    """Funktion, die die 5 neuesten Nachrichten von einer API abruft und deren Titel zurückgibt."""
    response = urequests.get(url)
    try:
        if response.status_code == 200:
            data = response.json()  # Konvertiert die Antwort in ein Python-Diktat
            feed = data.get('feed', [])  # Holt das 'feed' Array aus der Antwort

            # Extrahiert die Titel der ersten fünf Nachrichtenartikel
            titles = [article.get('title', 'Kein Titel verfügbar') for article in feed[:5]]
            return titles
        else:
            print('Fehler bei der Anfrage:', response.status_code)
            return [None]*5
    finally:
        response.close()