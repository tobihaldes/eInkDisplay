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
    'url': 'https://newsapi.org/v2/top-headlines?country=de&pageSize=6&apiKey=01cd449b036149ab84c94a7170eecc7b'
}

stock_config = {
    'symbol': 'AAPL',
    'api_token': '7I5ZTASNKQWHN3PT'
}

gallery_config = [
    {"type": "Weather_Tile_l", "x": 0, "y": 0},
    {"type": "ToDo_Tile", "x": 0, "y": 0},
    {"type": "Calendar_Tile", "x": 0, "y": 0},
    {"type": "News_Tile", "x": 0, "y": 0},
]

layout_config = [
    {"type": "Clock_Tile_s", "x": 560, "y": 0},
    {"type": "Weather_Tile_s", "x": 560, "y": 240},
]