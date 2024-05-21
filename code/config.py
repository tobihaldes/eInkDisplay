import tiles

wifi_config = {
    'ssid': 'Notebook von Tobi',
    'password': '1357924680'
}

weather_config = {
    'url': 'https://api.open-meteo.com/v1/forecast?latitude=49.1399&longitude=9.2205&daily=weather_code,temperature_2m_max,temperature_2m_min'
}

calendar_config = {
    'url': 'http://p139-caldav.icloud.com/published/2/MTE1NzQwNjE0NzQxMTU3NDmLjpu4-S1Y9s3ZY6FOrrHnIwf0-kAOhn-6sr24tcTFaqodbcvwQ-1iUIyMWm_Q-QI6qieG29wXJSUU0hdN6JI'
}

toDo_config = {
    'api_token': 'a7f3b805fdf80789ea5953f6d4eb7a799309a9b1',
    'project_id': '2332430307'
}


news_config = {
    'url': 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=COIN,CRYPTO:BTC,FOREX:USD&time_from=20220410T0130&limit=10&apikey=7I5ZTASNKQWHN3PT'
}

stock_config = {
    'symbol': 'AAPL',
    'api_token': '7I5ZTASNKQWHN3PT'
}

# Cycle throgh these tiles in the gallery using the next and previous Button (X, Y)
gallery = tiles.tile_gallery([
            #tiles.Weather_Tile_l(0,0),
            #tiles.ToDo_Tile(0,0),
            tiles.Calendar_Tile(0,0),
            tiles.News_Tile(0,0),
            ])

# Add static tiles that will be shown contiously (X, Y)
layout = [
            tiles.Clock_Tile_s(560, 0),
            tiles.Weather_Tile_s(560, 240),
            gallery,
         ]



