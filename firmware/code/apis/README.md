# Project API Documentation

This documentation provides an overview of the various APIs integrated within the project. Each section includes details on the functionalities provided by individual API scripts.

## Table of Contents

- [News API](#news-api)
- [Calendar API](#calendar-api)
- [Datetime API](#datetime-api)
- [Stocks API](#stocks-api)
- [ToDo API](#todo-api)
- [Weather API](#weather-api)
- [WiFi API](#wifi-api)

## News API

**File:** [`News.py`](/firmware/code/apis/News.py)

**Functionality:** Retrieves the latest news articles and returns their titles.

### Function: `get_latest_news(url)`

- **Description:** Makes a GET request to the provided URL, parses the JSON response, and extracts titles of the articles.
- **Parameters:**
  - `url` (string): URL of the news API endpoint.
- **Returns:** A list of titles for the first five news articles.
- **Usage:**
  ```python
  titles = get_latest_news("https://api.example.com/news")

## Calendar API

**File:** [`calendar.py`](/firmware/code/apis/calendar.py)

**Functionality:** Manages calendar events from iCalendar data.

### Function: `format_datetime(datetime_str)`

- **Description:** Formats iCalendar date/time strings into a more readable format.
- **Parameters:**
  - `datetime_str` (string): The iCalendar date/time string.
- **Returns:** Formatted date and time string.
- **Usage:**
  ```python
  formatted_datetime = format_datetime("20210101T120000")

## Datetime API

**File:** [`datetime.py`](/firmware/code/apis/datetime.py)

**Functionality:** Retrieves the current date and time from an API.

### Function: `get_date_and_time()`

- **Description:** Sends a GET request to a timekeeping API to fetch the current date and time, providing this crucial information in a format that can be directly utilized by other components of the application.
- **Returns:** A tuple containing the current date and time in separate strings (`date`, `time`), where `date` is formatted as `YYYY-MM-DD` and `time` as `HH:MM:SS`.
- **Usage:**
  ```python
  date, time = get_date_and_time()

## Stocks API

**File:** [`stocks.py`](/firmware/code/apis/stocks.py)

**Functionality:** Retrieves real-time stock price information.

### Function: `stock_price(symbol, api_key)`

- **Description:** Makes a GET request to a financial data API to fetch the current stock price for a given ticker symbol. The function extracts the specific price from the JSON response and formats it for display or further processing.
- **Parameters:**
  - `symbol` (string): The ticker symbol for the stock (e.g., "AAPL" for Apple Inc.).
  - `api_key` (string): Your API key for accessing the stock data service.
- **Returns:** A string representing the current price of the stock or an error message if the request fails.
- **Usage:**
  ```python
  price = stock_price("AAPL", "your_api_key_here")

## ToDo API

**File:** [`toDo.py`](/firmware/code/apis/toDo.py)

**Functionality:** Manages tasks from a project management tool API.

### Function: `toDoList(token, project_id)`

- **Description:** Retrieves a list of tasks with descriptions and due dates for a specified project.
- **Parameters:**
  - `token` (string): Authorization token.
  - `project_id` (string): Project identifier.
- **Returns:** A list of tasks with descriptions and due dates.
- **Usage:**
  ```python
  tasks = toDoList("your_auth_token", "your_project_id")

## Weather API

**File:** [`weather.py`](/firmware/code/apis/weather.py)

**Functionality:** Provides weather forecasts including temperature ranges and weather conditions.

### Function: `get_weather_forecast(api_url)`

- **Description:** Fetches weather forecasts from the specified API URL, including temperature ranges and weather conditions for the upcoming days.
- **Parameters:**
  - `api_url` (string): URL to the weather forecast API.
- **Returns:** A list of weather forecasts for the upcoming days.
- **Usage:**
  ```python
  forecast = get_weather_forecast("https://api.example.com/weather")

## WiFi API

**File:** [`wifi.py`](/firmware/code/apis/wifi.py)

**Functionality:** Manages WiFi connectivity to connect to networks.

### Function: `connect_to_wifi(ssid, password)`

- **Description:** Connects to a specified WiFi network using the provided SSID and password.
- **Parameters:**
  - `ssid` (string): The SSID of the WiFi network.
  - `password` (string): The password for the WiFi network.
- **Returns:** Boolean indicating the connection status.
- **Usage:**
  ```python
  connected = connect_to_wifi("NetworkSSID", "Password123")
