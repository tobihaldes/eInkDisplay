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
