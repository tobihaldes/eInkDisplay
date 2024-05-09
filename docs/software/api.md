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

**File:** `News.py`

**Functionality:** Retrieves the latest news articles and returns their titles.

### Function: `get_latest_news(url)`

- **Parameters:**
  - `url` (string): URL of the news API endpoint.
- **Returns:** A list of titles for the first five news articles.
- **Description:** 
  ```python
  Makes a GET request to the provided URL, parses the JSON response, and extracts titles of the articles.
