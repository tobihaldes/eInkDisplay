# Api config
wifi_config = {
    'ssid': 'Notebook von Tobi',
    'password': '1357924680'
}

weather_config = {
    'latitude': '49.1399',
    'longitude': '9.2205'
}

calendar_config = {
    'url': 'http://p139-caldav.icloud.com/published/2/MTE1NzQwNjE0NzQxMTU3NDmLjpu4-S1Y9s3ZY6FOrrHnIwf0-kAOhn-6sr24tcTFaqodbcvwQ-1iUIyMWm_Q-QI6qieG29wXJSUU0hdN6JI'
}

toDo_config = {
    'api_token': 'a7f3b805fdf80789ea5953f6d4eb7a799309a9b1',
    'project_id': '2332430307'
}


news_config = {
    'api_token': '01cd449b036149ab84c94a7170eecc7b',
    'country': 'de'
}

stock_config = {
    'symbol': 'AAPL',
    'api_token': '7I5ZTASNKQWHN3PT'
}


# Layout and tile config, place tiles at x,y
gallery_config = [
    {"type": "Weather_Tile_l", "x": 0, "y": 0},
    {"type": "ToDo_Tile", "x": 0, "y": 0},
    {"type": "Calendar_Tile", "x": 0, "y": 0},
    {"type": "News_Tile", "x": 0, "y": 0},
]

layout_config = [
    {"type": "Clock_Tile_s", "x": 560, "y": 0},
    {"type": "Weather_Tile_s", "x": 560, "y": 240},
    {"type": "gallery"},
]