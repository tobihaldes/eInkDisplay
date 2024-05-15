## File Descriptions

### config.py

This file contains configuration parameters for the various services used by the dashboard.

- **wifi_config**: Stores the SSID and password for the Wi-Fi connection.
  ```python
  wifi_config = {
      'ssid': 'xxxxxxx',
      'password': '******'
  }
  ```

- **weather_config**: Contains the URL for fetching weather data.
  ```python
  weather_config = {
      'url': 'https://api.open-meteo.com/v1/forecast?latitude=49.1399&longitude=9.2205&daily=weather_code,temperature_2m_max,temperature_2m_min'
  }
  ```

- **calendar_config**: Contains the URL for fetching calendar events.
  ```python
  calendar_config = {
      'url': 'http://p139-caldav.icloud.com/published/2/MTE1NzQwNjE0NzQxMTU3NDmLjpu4-S1Y9s3ZY6FOrrHnIwf0-kAOhn-6sr24tcTFaqodbcvwQ-1iUIyMWm_Q-QI6qieG29wXJSUU0hdN6JI'
  }
  ```

- **toDo_config**: Stores the API token and project ID for fetching to-do lists.
  ```python
  toDo_config = {
      'api_token': 'a7f3b805fdf80789ea5953f6d4eb7a799309a9b1',
      'project_id': '2332430307'
  }
  ```

- **news_config**: Contains the URL for fetching news.
  ```python
  news_config = {
      'url': 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=COIN,CRYPTO:BTC,FOREX:USD&time_from=20220410T0130&limit=10&apikey=7I5ZTASNKQWHN3PT'
  }
  ```

- **stock_config**: Stores the stock symbol and API token for fetching stock prices.
  ```python
  stock_config = {
      'symbol': 'AAPL',
      'api_token': '7I5ZTASNKQWHN3PT'
  }
  ```
