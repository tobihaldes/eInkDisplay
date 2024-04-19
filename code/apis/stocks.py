import urequests

def stock_price(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    try:
        response = urequests.get(url)
        if response.status_code == 200:
            data = response.json()
            stock_info = data['Global Quote']
            price = stock_info['05. price']
            print(f"Aktueller Kurs von {symbol}: {price}")
        else:
            print("Fehler bei der Anfrage: Status-Code", response.status_code)
    except Exception as error:
        print("Ein Fehler ist aufgetreten:", error)
    finally:
        if 'response' in locals():
            response.close()
