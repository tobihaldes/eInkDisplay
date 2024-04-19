import urequests

def stock_price(api_key):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AAPL&apikey={api_key}"
    try:
        response = urequests.get(url)
        if response.status_code == 200:
            data = response.json()
            stock_info = data['Global Quote']
            price = stock_info['05. price']
            print("Aktueller Kurs von Apple (AAPL):", price)
        else:
            print("Fehler bei der Anfrage: Status-Code", response.status_code)
    except Exception as error:
        print("Ein Fehler ist aufgetreten:", error)
    finally:
        response.close()
