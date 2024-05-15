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

**File:** [`News.py`](/code/apis/News.py)

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

**File:** [`calendar.py`](/code/apis/calendar.py)

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

**File:** [`datetime.py`](/code/apis/datetime.py)

**Functionality:** Retrieves the current date and time from an API.

### Function: `get_date_and_time()`

- **Description:** Sends a GET request to a timekeeping API to fetch the current date and time, providing this crucial information in a format that can be directly utilized by other components of the application.
- **Returns:** A tuple containing the current date and time in separate strings (`date`, `time`), where `date` is formatted as `YYYY-MM-DD` and `time` as `HH:MM:SS`.
- **Usage:**
  ```python
  date, time = get_date_and_time()

## Stocks API

**File:** [`stocks.py`](/code/apis/stocks.py)

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


