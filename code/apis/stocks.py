import urequests

def stock_price(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    try:
        response = urequests.get(url)
        if response.status_code == 200:
            data = response.json()
            stock_info = data['Global Quote']
            price = stock_info['05. price']
            result= "Kurs von "+ symbol + ": " + price
        else:
            result= "Fehler bei der Anfrage: " + response.status_code
    except Exception as error:
        result = "Ein Fehler ist aufgetreten: "+ error
    finally:
        if 'response' in locals():
            response.close()
        return result
