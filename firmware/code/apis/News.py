import urequests
import gc

def get_latest_news(api_token, country):
    
    url= f'https://newsapi.org/v2/top-headlines?country={country}&pageSize=6&apiKey={api_token}'
    
    gc.collect()
    headers = {
    'User-Agent': 'eInkDisplay'
    }
    
    response = None
    
    try:
        response = urequests.get(url, headers=headers)
        print(response.json())
        if response.status_code == 200:
            data = response.json()  # Konvertiert die Antwort in ein Python-Diktat
            articles = data.get('articles', [])  # Holt das 'articles' Array aus der Antwort

            # Extrahiert die Titel der ersten fünf Nachrichtenartikel
            titles = [article.get('title', 'Kein Titel verfuegbar') for article in articles[:6]]
            return titles
        else:
            print('Fehler bei der Anfrage:', response.status_code)
            titles = ['Kein Titel verfuegbar' for _ in range(6)]
            return titles
    except OSError as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        titles = ['Kein Titel verfuegbar' for _ in range(6)]
        return titles
    finally:
        # Die Verbindung schließen, wenn sie geöffnet wurde
        if response is not None:
            try:
                response.close()
            except AttributeError:
                pass  # Falls response.close() fehlschlägt, nichts tun