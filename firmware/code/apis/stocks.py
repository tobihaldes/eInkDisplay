import urequests

def stock_price(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    response = None
    try:
        response = urequests.get(url)
        if response.status_code == 200:
            data = response.json()
            stock_info = data['Global Quote']
            price = stock_info['05. price']
            result= "Kurs von "+ symbol + ": " + price
            return result
        else:
            result= "Fehler bei der Anfrage: " + response.status_code
            return result
    except Exception as error:
        result = "Ein Fehler ist aufgetreten: "+ str(error)
        return result
    finally:
        # Die Verbindung schließen, wenn sie geöffnet wurde
        if response is not None:
            try:
                response.close()
            except AttributeError:
                pass  # Falls response.close() fehlschlägt, nichts tun
