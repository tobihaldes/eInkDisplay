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

  ### driver.py

This file contains the driver for the E-Ink display. The driver is based on a driver provided by Waveshare but has been customized for this project.

#### Customizations in driver.py

- **RAM Allocation**: Modifications have been made to allocate RAM for large byte arrays first to avoid heap fragmentation.
  ```python
  buffer_black = bytearray(48000)
  buffer_red = bytearray(48000)
  ```

- **Display Initialization**: Customizations to handle display hardware initialization and prevent memory issues.
  ```python
  class EPD_7in5_B:
      def __init__(self, tiles):
          global buffer_black, buffer_red
          self.tiles = tiles
          self.buffer_black = buffer_black
          self.buffer_red = buffer_red
          ...
  ```

- **Custom Methods**:
  - **refresh_framebuffer**: Updates the framebuffer with the current data from the tiles.
    ```python
    def refresh_framebuffer(self):
        self.imageblack.fill(0xff)
        self.imagered.fill(0x00)
        
        for tile in self.tiles:
            if not isinstance(tile, tiles.Tile):
                raise TypeError("Invalid tile type passed.")
            tile.draw_canvas(self)
    ```

  - **init**: Customizations to initialize the Wi-Fi connection and retrieve configuration data.
    ```python
    def init(self):
        ...
        result = connect_to_wifi(config.wifi_config['ssid'], config.wifi_config['password'])
        print("Connection status:", result)
        ...
    ```
### icons.py

This file defines various icons that can be displayed on the E-Ink display.

- **Icon Class**: Contains byte arrays for different icons (e.g., sun, cloud) used in the weather display.
  ```python
  class Icon():
      sun_data = bytearray([...])
      bewoelkt_data = bytearray([...])
      cloud_data = bytearray([...])
  ```

- **draw_icon Method**: Creates FrameBuffers for the icons.
  ```python
  def draw_icon(self, icon):
      if icon == "sun":
          icon_fb = framebuf.FrameBuffer(self.sun_data, 100, 100, framebuf.MONO_HLSB)
      elif icon == "bewoelkt":
          icon_fb = framebuf.FrameBuffer(self.bewoelkt_data, 100, 100, framebuf.MONO_HLSB)
      elif icon == "wolke":
          icon_fb = framebuf.FrameBuffer(self.cloud_data, 100, 100, framebuf.MONO_HLSB)
      return icon_fb
  ```
### main.py

The main file of the project. It initializes the system and contains the logic for displaying various tiles of information on the E-Ink display.

- **Button Initialization**: Configures buttons for navigating between tiles.
  ```python
  btn_next = Button(3)
  btn_next.when_pressed = button_next
  btn_prev = Button(2)
  btn_prev.when_pressed = button_prev
  ```

- **Layout Definition**: Defines the layout of the tiles to be displayed.
  ```python
  gallery = tiles.tile_gallery([
          tiles.Calendar_Tile(0,0),
          tiles.News_Tile(0,0),
      ])
  
  layout = [
      tiles.Clock_Tile_s(560, 0),
      tiles.Weather_Tile_s(560, 240),
      gallery,
  ]
  ```

- **Display Logic**: Contains the main loop for updating the display and handling button events.
  ```python
  while True:
      update_flag = 60
      display.init()
      display.display()
      display.delay_ms(1000)
      display.sleep()
      display.delay_ms(1000)
      while update_flag > 0:
          update_flag -= 1
          time.sleep(1)
  ```

