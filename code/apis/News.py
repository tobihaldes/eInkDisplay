import urequests

url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=COIN,CRYPTO:BTC,FOREX:USD&time_from=20220410T0130&limit=10&apikey=7I5ZTASNKQWHN3PT'

response = urequests.get(url)

if response.status_code == 200:
    data = response.json()  # Konvertiert die Antwort in ein Python-Diktat
    feed = data.get('feed', [])  # Holt das 'feed' Array aus der Antwort

    # Iteriert über die ersten fünf Einträge im 'feed' Array und druckt ihre Titel
    for article in feed[:5]:
        print(article.get('title', 'Kein Titel verfügbar'))  # Druckt den Titel jedes Artikels

else:
    print('Fehler bei der Anfrage:', response.status_code)

response.close()
