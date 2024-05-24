import framebuf
import config
import icons
import gc
from apis.datetime import get_date_and_time
from apis.weather import get_weather_forecast
from apis.toDo import toDoList
from apis.calendar import get_next_events
from apis.News import get_latest_news
from apis.stocks import stock_price

black = 0x00
red = 0xff

# Parent class that defines Basic function for all tiles
class Tile():
    width = 100
    height = 100
    
    def __init__(self, x, y):
        self.y = y
        self.x = x
        
    def draw_canvas(self, can):
        can.imagered.fill(0x00)
        can.imageblack.fill(0xff)
    
    def replace_umlaute(text):
    # replace die Umlaute durch die entsprechenden Zeichenfolgen
        text = text.replace('ä', 'ae')
        text = text.replace('ö', 'oe')
        text = text.replace('ü', 'ue')
        text = text.replace('Ä', 'Ae')
        text = text.replace('Ö', 'Oe')
        text = text.replace('Ü', 'Ue')
        text = text.replace('ß', 'ss')
    
        return text

class tile_gallery(Tile):
    def __init__(self, tiles):
        self.tiles= tiles
        self.num_tiles = len(tiles)
        self.current_index = 0
    
    def next_tile(self):
        self.current_index = (self.current_index + 1) % self.num_tiles

    def prev_tile(self):
        self.current_index = (self.current_index - 1) % self.num_tiles
    
    def draw_canvas(self, can):
        print(self.tiles[self.current_index])
        self.tiles[self.current_index].draw_canvas(can)
        
      
class Clock_Tile_s(Tile):
    
    width = 240
    height = 240
    
    def draw_canvas(self, can):
        i = 1
        #Parameter für Stunden und Minuten
        gc.collect()
        date, time = get_date_and_time();
        gc.collect()
        timeHour, minute, second = time.split(':')
        
        minute = int(minute)
        timeHour = int(timeHour)
        
        # Minute Quarter anhand der Minute herausfinden
        if minute <= 15:
            minuteQuarter = 1
        elif minute <= 30:
            minuteQuarter = 2
        elif minute <= 45:
            minuteQuarter = 3
        elif minute <= 60:
            minuteQuarter = 4

        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
        
        #Stundenzahlen
        #can.imageblack.text(timeHour, self.x+120, self.y+120, black)
        #Stundenzahlen
#         if timeHour == 1:
#             #Z1oben
#             can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
#             #Z1links oben
#             can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1links unten
#             can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             #Z1unten
#             can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)  
#         
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
#         elif timeHour == 2:
#             #Z1oben
#             can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
#             #Z1links oben
#             can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1links unten
#             can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             #Z1unten
#             can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2links unten
#             can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
#             #Z2unten
#             can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
#         elif timeHour == 3:
#             #Z1oben
#             can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
#             #Z1links oben
#             can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1links unten
#             can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             #Z1unten
#             can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2links unten
#             can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
#             #Z2unten
#             can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
#         elif timeHour == 4:
#             #Z1oben
#             can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
#             #Z1links oben
#             can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1links unten
#             can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             #Z1unten
#             can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2links oben
#             can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
#         elif timeHour == 5:
#             #Z1oben
#             can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
#             #Z1links oben
#             can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1links unten
#             can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             #Z1unten
#             can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#              #Z2links oben
#             can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
#             #Z2unten
#             can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
#         elif timeHour == 6:
#             #Z1oben
#             can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
#             #Z1links oben
#             can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1links unten
#             can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             #Z1unten
#             can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2links oben
#             can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2links unten
#             can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
#             #Z2unten
#             can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
#         elif timeHour == 7:
#             #Z1oben
#             can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
#             #Z1links oben
#             can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1links unten
#             can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             #Z1unten
#             can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
#         elif timeHour == 8:
#             #Z1oben
#             can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
#             #Z1links oben
#             can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1links unten
#             can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             #Z1unten
#             can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2unten
#             can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
#             #Z2links oben
#             can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2links unten
#             can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)  
#         elif timeHour == 9:
#             #Z1oben
#             can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
#             #Z1links oben
#             can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1links unten
#             can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             #Z1unten
#             can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2unten
#             can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
#             #Z2links oben
#             can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)  
#         elif timeHour == 10:
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2unten
#             can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
#             #Z2links oben
#             can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2links unten
#             can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True) 
#         elif timeHour == 11:
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True) 
#         elif timeHour == 12:
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2links unten
#             can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
#             #Z2unten
#             can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
#         elif timeHour == 13:
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2links unten
#             can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
#             #Z2unten
#             can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
#         elif timeHour == 14:
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             
#             #Z2links oben
#             can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
#         elif timeHour == 15:
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#              #Z2links oben
#             can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
#             #Z2unten
#             can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
#         elif timeHour == 16:
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2links oben
#             can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2links unten
#             can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
#             #Z2unten
#             can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
#         elif timeHour == 17:
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
#         elif timeHour == 18:
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2unten
#             can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
#             #Z2links oben
#             can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2links unten
#             can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)  
#         elif timeHour == 19:
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1rechts unten
#             can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2unten
#             can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
#             #Z2links oben
#             can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)  
#         elif timeHour == 20:
#             #Z1oben
#             can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1mitte
#             can.imageblack.rect(self.x+85, self.y+117, 30, 6, black, True)
#             #Z1links unten
#             can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
#             #Z1unten
#             can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2unten
#             can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
#             #Z2links oben
#             can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2links unten
#             can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True) 
#         elif timeHour == 21:
#             #Z1oben
#             can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1mitte
#             can.imageblack.rect(self.x+85, self.y+117, 30, 6, black, True)
#             #Z1links unten
#             can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
#             #Z1unten
#             can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
#             
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
#         elif timeHour == 22:
#             #Z1oben
#             can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1mitte
#             can.imageblack.rect(self.x+85, self.y+117, 30, 6, black, True)
#             #Z1links unten
#             can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
#             #Z1unten
#             can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2links unten
#             can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
#             #Z2unten
#             can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
#         elif timeHour == 23:
#             #Z1oben
#             can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1mitte
#             can.imageblack.rect(self.x+85, self.y+117, 30, 6, black, True)
#             #Z1links unten
#             can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
#             #Z1unten
#             can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
#             
#             #Z2oben
#             can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2links unten
#             can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
#             #Z2unten
#             can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
#         elif timeHour == 24:
#             #Z1oben
#             can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
#             #Z1rechts oben
#             can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
#             #Z1mitte
#             can.imageblack.rect(self.x+85, self.y+117, 30, 6, black, True)
#             #Z1links unten
#             can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
#             #Z1unten
#             can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
#             
#             #Z2links oben
#             can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
#             #Z2rechts oben
#             can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
#             #Z2mitte
#             can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
#             #Z2rechts unten
#             can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
# 
# 
# 
# 
#         
#             
#         #Viertelstunden Zeiger 
#         if minuteQuarter == 1:
#             can.imagered.ellipse(self.x+120, self.y+120, 107, 107, red, True, 1)
#         elif minuteQuarter ==2:
#             can.imagered.ellipse(self.x+120, self.y+120, 107, 107, red, True, 9)
#         elif minuteQuarter ==3:
#             can.imagered.ellipse(self.x+120, self.y+120, 107, 107, red, True, 13)
#         elif minuteQuarter ==4:
#             can.imagered.ellipse(self.x+120, self.y+120, 107, 107, red, True, 15)
#                 
#         can.imageblack.ellipse(self.x+120, self.y+120, 108, 108, black, False)
#         can.imageblack.ellipse(self.x+120, self.y+120, 100, 100, black)
#         can.imagered.ellipse(self.x+120, self.y+120, 100, 100, 0x00, True)
#         #Ziffernblatt oben und unten
#         can.imageblack.rect(self.x+118, self.y+25, 4, 20, black, True)
#         can.imageblack.rect(self.x+118, self.y+195, 4, 20, black, True)
#         #Ziffernblatt links und rechts
#         can.imageblack.rect(self.x+25, self.y+118, 20, 4, black, True)
#         can.imageblack.rect(self.x+195, self.y+118, 20, 4, black, True)
#         #Ziffernblatt kleine Striche
#         can.imageblack.line(self.x+171-5, self.y+33+5, self.x+158, self.y+53, black)
#         can.imageblack.line(self.x+208-5, self.y+69+5, self.x+186, self.y+82, black)
#         can.imageblack.line(self.x+208-5, self.y+171-5, self.x+186, self.y+158, black)
#         can.imageblack.line(self.x+171-5, self.y+208-5, self.x+158, self.y+186, black)
#         can.imageblack.line(self.x+69+5, self.y+208-5, self.x+82, self.y+186, black)
#         can.imageblack.line(self.x+33+5, self.y+171-5, self.x+53, self.y+158, black)
#         can.imageblack.line(self.x+33+5, self.y+69+5, self.x+53, self.y+82, black)
#         can.imageblack.line(self.x+69+5, self.y+33+5, self.x+82, self.y+53, black)   
    
class Weather_Tile_s(Tile):
    width = 240
    height = 240
    
    def draw_canvas(self, can):
        
        gc.collect()
        #Get weather data
        weather_forecast = get_weather_forecast(config.weather_config['latitude'], config.weather_config['longitude'])
        gc.collect()
        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
        can.imageblack.text("Date: " + weather_forecast[0]['date'], self.x+50, self.y+16, black)
        can.imagered.text("Max temperature: " + weather_forecast[0]['max_temp'], self.x+45, self.y+211, red)
        can.imageblack.text("Min temperature: " + weather_forecast[0]['min_temp'], self.x+45, self.y+226, black)
        weather_icon = weather_forecast[0]['weathercode']
        Weather_Tile_l.draw_weather_tile(can, weather_icon, self.x, self.y, 27, 0)
        
      
        y_row_counter = 0
        row_count = 0
        max_rows = 4
        cols = 210 // 8 #Breite des Textfeldes
        current_row = ''
        last_space_index = -1  
        text = "Weatherstatus: "+ Tile.replace_umlaute(weather_forecast[0]['weather'])+" "
        
        for i in range(len(text)):
            current_row += text[i]
            if text[i] == ' ':
                last_space_index = i  
            if len(current_row) == cols or (i == len(text) - 1):  # Wenn die maximale Spaltenbreite erreicht ist.
                # Zeichne die aktuelle Zeile bis zum letzten Leerzeichen
                can.imageblack.text(current_row[:last_space_index], self.x+12, self.y+161 + y_row_counter, black)
                # Entferne den Teil, der bereits gezeichnet wurde, aus dem aktuellen Text
                current_row = current_row[last_space_index + 1:]
                y_row_counter += 8  # Zeilenhöhe
                row_count += 1
                last_space_index = -1 
                if row_count >= max_rows:
                    break
        # Zeichne den Rest der letzten Zeile, wenn sie nicht vollständig war
        if current_row:
            can.imageblack.text(current_row, self.x+12, self.y+161 + y_row_counter, black)
        
    
class Weather_Tile_l(Tile):
    width = 560
    height = 480
    
    def draw_weather_tile(can, weather_code, x, y, x_cords, y_cords):
        if weather_code == 0:
            can.imageblack.blit(icons.Icon.draw_icon("sun"), x + x_cords + 43, y + y_cords + 40)
        elif weather_code == 1 or weather_code == 2:
            can.imageblack.blit(icons.Icon.draw_icon("cloudy"), x + x_cords + 43, y + y_cords + 40)
        elif weather_code == 3:
            can.imageblack.blit(icons.Icon.draw_icon("cloud"), x + x_cords + 43, y + y_cords + 40)
        elif weather_code == 45 or weather_code == 48:
            can.imageblack.blit(icons.Icon.draw_icon("fog"), x + x_cords + 43, y + y_cords + 40)
        elif (weather_code > 50 and weather_code < 68) or (weather_code >= 80 and weather_code < 87):
            can.imageblack.blit(icons.Icon.draw_icon("rain"), x + x_cords + 43, y + y_cords + 40)
        elif weather_code == 95 or weather_code == 99 or weather_code == 96:
            can.imageblack.blit(icons.Icon.draw_icon("storm"), x + x_cords + 43, y + y_cords + 40)
        elif weather_code > 70 and weather_code < 78:
            can.imageblack.blit(icons.Icon.draw_icon("snow"), x + x_cords + 43, y + y_cords + 40)
        else:
            can.imageblack.rect(x+x_cords, y+y_cords, 100, 100, black, False)
            print("Weather_Code when no icon found: " + str(weather_code))

    
    def draw_canvas(self, can):
        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
        #Footer
        can.imageblack.rect(self.x+0, self.y+470, 560, 10, black, True)
        can.imagered.text("< News",self.x+1, self.y+471, red)
        can.imagered.text("Weather",self.x+250, self.y+471, red)
        can.imagered.text("ToDo >",self.x+510, self.y+471, red)
        
        
        #Gitternetzlinien Horizontal
        can.imageblack.rect(self.x+10, self.y+240, 540, 2, black, True)
        
        gc.collect()
        #Get weather data
        weather_forecast = get_weather_forecast(config.weather_config['latitude'], config.weather_config['longitude'])
        gc.collect()
        
        weather_x_cords = [0, 187, 374, 0, 187, 374]
        weather_y_cords = [0, 0, 0, 242, 242, 242]
        weather_dates = ["Date: " + weather_forecast[1]['date'], "Date: " + weather_forecast[2]['date'], "Date: " + weather_forecast[3]['date'], "Date: " + weather_forecast[4]['date'], "Date: " + weather_forecast[5]['date'], "Date: " + weather_forecast[6]['date']]
        temp_high = [weather_forecast[1]['max_temp'], weather_forecast[2]['max_temp'], weather_forecast[3]['max_temp'], weather_forecast[4]['max_temp'], weather_forecast[5]['max_temp'], weather_forecast[6]['max_temp']]
        temp_low = [weather_forecast[1]['min_temp'], weather_forecast[2]['min_temp'], weather_forecast[3]['min_temp'], weather_forecast[4]['min_temp'], weather_forecast[5]['min_temp'], weather_forecast[6]['min_temp']]
        weather_status = [weather_forecast[1]['weather'], weather_forecast[2]['weather'], weather_forecast[3]['weather'], weather_forecast[4]['weather'], weather_forecast[5]['weather'], weather_forecast[6]['weather']]
        weather_icon = [weather_forecast[1]['weathercode'], weather_forecast[2]['weathercode'], weather_forecast[3]['weathercode'], weather_forecast[4]['weathercode'], weather_forecast[5]['weathercode'], weather_forecast[6]['weathercode']]
        k=0
        for i in range(6):
            can.imageblack.rect(self.x+weather_x_cords[k]-2, self.y+weather_y_cords[k]+10, 2, 220, black, True)
            can.imageblack.text(weather_dates[k], self.x+weather_x_cords[k]+25, self.y+weather_y_cords[k]+15, black)
            can.imagered.text("Max temp.: "+str(temp_high[k]), self.x+weather_x_cords[k]+25, self.y+weather_y_cords[k]+200, red)
            can.imageblack.text("Min temp.: "+str(temp_low[k]), self.x+weather_x_cords[k]+25, self.y+weather_y_cords[k]+215, black)
            
            y_row_counter = 0
            row_count = 0
            max_rows = 4
            cols = 170 // 8 #Breite des Textfeldes
            current_row = ''
            last_space_index = -1  
            text = Tile.replace_umlaute(weather_status[k])+" "
            for i in range(len(text)):
                current_row += text[i]
                if text[i] == ' ':
                    last_space_index = i  
                if len(current_row) == cols or (i == len(text) - 1):  # Wenn die maximale Spaltenbreite erreicht ist.
                    # Zeichne die aktuelle Zeile bis zum letzten Leerzeichen
                    can.imageblack.text(current_row[:last_space_index], 12 + weather_x_cords[k], 160 + weather_y_cords[k] + y_row_counter, black)
                    # Entferne den Teil, der bereits gezeichnet wurde, aus dem aktuellen Text
                    current_row = current_row[last_space_index + 1:]
                    y_row_counter += 8  # Zeilenhöhe
                    row_count += 1
                    last_space_index = -1 
                    if row_count >= max_rows:
                        break
            # Zeichne den Rest der letzten Zeile, wenn sie nicht vollständig war
            if current_row:
                can.imageblack.text(current_row, 12 + weather_x_cords[k], 160 + weather_y_cords[k] + y_row_counter, black) 
            Weather_Tile_l.draw_weather_tile(can, weather_icon[k], self.x, self.y, weather_x_cords[k], weather_y_cords[k])
            k=k+1
            if k>99:
                break
    
class ToDo_Tile(Tile):
    width = 560
    height = 480
    def draw_canvas(self, can):
        gc.collect()
        #get Tasks:
        tasks = toDoList(config.toDo_config['api_token'], config.toDo_config['project_id'])        
        gc.collect()
        print(tasks)
        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
        
        #Footer
        can.imageblack.rect(self.x+0, self.y+470, 560, 10, black, True)
        can.imagered.text("< Weather",self.x+1, self.y+471, red)
        can.imagered.text("ToDo",self.x+260, self.y+471, red)
        can.imagered.text("Calendar >",self.x+480, self.y+471, red)
        
        todo_x_cords = [5, 190, 375, 5, 190, 375, 5, 190, 375, 5, 190, 375]
        todo_y_cords = [5, 5, 5, 120, 120, 120, 235, 235, 235, 350, 350, 350]
        todo_data = [["Task: " + tasks[0][0], "Due to: " + tasks[0][1]], ["Task: " + tasks[1][0], "Due to: " + tasks[1][1]], ["Task: " + tasks[2][0], "Due to: " + tasks[2][1]], ["Task: " + tasks[3][0], "Due to: " + tasks[3][1]], ["Task: " + tasks[4][0], "Due to: " + tasks[4][1]], ["Task: " + tasks[5][0], "Due to: " + tasks[5][1]], ["Task: " + tasks[6][0], "Due to: " + tasks[6][1]], ["Task: " + tasks[7][0], "Due to: " + tasks[7][1]], ["Task: " + tasks[8][0], "Due to: " + tasks[8][1]], ["Task: " + tasks[9][0], "Due to: " + tasks[9][1]], ["Task: " + tasks[10][0], "Due to: " + tasks[10][1]]]
        k=0
        for i in range(len(todo_data)):
            can.imageblack.rect(self.x+todo_x_cords[k], self.y+todo_y_cords[k], 180, 110, black, False)
            can.imageblack.line(self.x+todo_x_cords[k]+ 159, self.y+todo_y_cords[k], self.x+todo_x_cords[k]+179, self.y+todo_y_cords[k]+20, black)
            can.imageblack.text("ToDo Nr. "+str(k+1), self.x+todo_x_cords[k]+ 5, self.y+todo_y_cords[k]+ 5, black)
            can.imagered.text(todo_data[k][1], self.x+todo_x_cords[k]+ 5, self.y+todo_y_cords[k]+ 100, red)
            can.imageblack.line(self.x+todo_x_cords[k]+ 0, self.y+todo_y_cords[k]+95, self.x+todo_x_cords[k]+179, self.y+todo_y_cords[k]+95, black)
            
            y_row_counter = 0
            row_count = 0
            max_rows = 8
            cols = 170 // 8 #Breite des Textfeldes
            current_row = ''
            last_space_index = -1
            text = Tile.replace_umlaute(todo_data[k][0])+" " 
            for i in range(len(text)):
                current_row += text[i]
                if text[i] == ' ':
                    last_space_index = i  
                if len(current_row) == cols or (i == len(text) - 1):  # Wenn die maximale Spaltenbreite erreicht ist.
                    # Zeichne die aktuelle Zeile bis zum letzten Leerzeichen
                    can.imageblack.text(current_row[:last_space_index], 5 + todo_x_cords[k], 20 + todo_y_cords[k] + y_row_counter, black)
                    # Entferne den Teil, der bereits gezeichnet wurde, aus dem aktuellen Text
                    current_row = current_row[last_space_index + 1:]
                    y_row_counter += 10  # Zeilenhöhe
                    row_count += 1
                    last_space_index = -1 
                    if row_count >= max_rows:
                        break
            # Zeichne den Rest der letzten Zeile, wenn sie nicht vollständig war
            if current_row:
                can.imageblack.text(current_row, 5 + todo_x_cords[k], 20 + todo_y_cords[k] + y_row_counter, black) 
            k=k+1
            if k>13:
                break
        
class Calendar_Tile(Tile):
    width = 560
    height = 480
    def draw_canvas(self, can):
        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
        can.imageblack.rect(self.x+279, self.y+5, 2, 455, black, True)
        #Footer
        can.imageblack.rect(self.x+0, self.y+470, 560, 10, black, True)
        can.imagered.text("< ToDo",self.x+1, self.y+471, red)
        can.imagered.text("Calendar",self.x+250, self.y+471, red)
        can.imagered.text("News >",self.x+510, self.y+471, red)
        
        todo_x_cords = [5, 5, 5, 5, 285, 285, 285, 285]
        todo_y_cords = [5, 120, 235, 350, 5, 120, 235, 350]
        
        #get Calendar Data
        gc.collect()
        events = get_next_events(config.calendar_config['url'])
        gc.collect()
        if len(events) >= 5:
            calendar_data = [["Appointment: ", events[0]['summary'], events[0]['start_time']], ["Appointment: ", events[1]['summary'], events[1]['start_time']], ["Appointment: ", events[2]['summary'], events[2]['start_time']], ["Appointment: ", events[3]['summary'], events[3]['start_time']], ["Appointment: ", events[4]['summary'], events[4]['start_time']]]
        else:
            # Handhabung, falls nicht genügend Events vorhanden sind
            calendar_data = [["No Appointment found", "No Data", "N/A"]] * 5  # Erstellt eine Liste mit Platzhaltern
        k=0
        for i in range(len(calendar_data)):
            can.imageblack.rect(self.x+todo_x_cords[k], self.y+todo_y_cords[k], 270, 110, black, False)
            
            can.imageblack.text(calendar_data[k][0]+str(k+1), self.x+todo_x_cords[k]+ 5, self.y+todo_y_cords[k]+ 5, black)
            can.imagered.text(calendar_data[k][2], self.x+todo_x_cords[k]+ 5, self.y+todo_y_cords[k]+ 100, red)
            can.imageblack.line(self.x+todo_x_cords[k]+ 0, self.y+todo_y_cords[k]+95, self.x+todo_x_cords[k]+269, self.y+todo_y_cords[k]+95, black)
            
            y_row_counter = 0
            row_count = 0
            max_rows = 8
            cols = 260 // 8 #Breite des Textfeldes
            current_row = ''
            last_space_index = -1
            text = Tile.replace_umlaute(calendar_data[k][1])+" "
            for i in range(len(text)):
                current_row += text[i]
                if text[i] == ' ':
                    last_space_index = i  
                if len(current_row) == cols or (i == len(text) - 1):  # Wenn die maximale Spaltenbreite erreicht ist.
                    # Zeichne die aktuelle Zeile bis zum letzten Leerzeichen
                    can.imageblack.text(current_row[:last_space_index], 5 + todo_x_cords[k], 20 + todo_y_cords[k] + y_row_counter, black)
                    # Entferne den Teil, der bereits gezeichnet wurde, aus dem aktuellen Text
                    current_row = current_row[last_space_index + 1:]
                    y_row_counter += 10  # Zeilenhöhe
                    row_count += 1
                    last_space_index = -1 
                    if row_count >= max_rows:
                        break
            # Zeichne den Rest der letzten Zeile, wenn sie nicht vollständig war
            if current_row:
                can.imageblack.text(current_row, 5 + todo_x_cords[k], 20 + todo_y_cords[k] + y_row_counter, black) 
            k=k+1
            if k>7:
                break
        
class News_Tile(Tile):
    width = 560
    height = 480
    def draw_canvas(self, can):
        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
        can.imageblack.rect(self.x+279, self.y+5, 2, 455, black, True)
        #Footer
        can.imageblack.rect(self.x+0, self.y+470, 560, 10, black, True)
        can.imagered.text("< Calendar",self.x+1, self.y+471, red)
        can.imagered.text("News",self.x+265, self.y+471, red)
        can.imagered.text("Weather >",self.x+485, self.y+471, red)
        
        todo_x_cords = [5, 5, 5, 5, 285, 285, 285, 285]
        todo_y_cords = [5, 120, 235, 350, 5, 120, 235, 350]
        
        #Abfrage der News
        gc.collect()
        news_titles = get_latest_news(config.news_config['api_token'], config.news_config['country'])
        gc.collect()
        #Aufrufen der News
        #news_titles[0]   #Baut sich folgendermaßen auf: ('title', 'Kein Titel verfügbar')
        #Da aber News-Tile noch nicht fertig ist, noch auskommentiert.
        
        #Abfrage für Aktienkurs
        price = stock_price(config.stock_config['symbol'], config.stock_config['api_token'])
        #muss nur noch angezeigt werden, nach absprache mit Design Team.
        news_data =[news_titles[0], news_titles[1], news_titles[2], news_titles[3], news_titles[4], news_titles[5]]
        k=0
        date, time = get_date_and_time();
        can.imagered.rect(self.x+todo_x_cords[7], self.y+todo_y_cords[7], 270, 110, red, False)   
        can.imageblack.text("Share price for " + config.stock_config['symbol'] + " : ", self.x+todo_x_cords[7]+ 5, self.y+todo_y_cords[7]+ 5, black)
        can.imageblack.text(price, self.x+todo_x_cords[7]+ 5, self.y+todo_y_cords[7]+ 20, black)
        can.imagered.text("Updated: " + date, self.x+todo_x_cords[7]+ 5, self.y+todo_y_cords[7]+ 100, red)
        can.imageblack.line(self.x+todo_x_cords[7]+ 0, self.y+todo_y_cords[7]+95, self.x+todo_x_cords[7]+269, self.y+todo_y_cords[7]+95, black)
        
        for i in range(len(news_data)):
            can.imageblack.rect(self.x+todo_x_cords[k], self.y+todo_y_cords[k], 270, 110, black, False)
            
            can.imageblack.text("Headline: ", self.x+todo_x_cords[k]+ 5, self.y+todo_y_cords[k]+ 5, black)
            #can.imagered.text(news_data[k][1], self.x+todo_x_cords[k]+ 5, self.y+todo_y_cords[k]+ 100, red)
            #can.imageblack.line(self.x+todo_x_cords[k]+ 0, self.y+todo_y_cords[k]+95, self.x+todo_x_cords[k]+269, self.y+todo_y_cords[k]+95, black)
            
            y_row_counter = 0
            row_count = 0
            max_rows = 8
            cols = 260 // 8 #Breite des Textfeldes
            current_row = ''
            last_space_index = -1
            text = Tile.replace_umlaute(news_data[k])+" " 
            for i in range(len(text)):
                current_row += text[i]
                if text[i] == ' ':
                    last_space_index = i  
                if len(current_row) == cols or (i == len(text) - 1):  # Wenn die maximale Spaltenbreite erreicht ist.
                    # Zeichne die aktuelle Zeile bis zum letzten Leerzeichen
                    can.imageblack.text(current_row[:last_space_index], 5 + todo_x_cords[k], 20 + todo_y_cords[k] + y_row_counter, black)
                    # Entferne den Teil, der bereits gezeichnet wurde, aus dem aktuellen Text
                    current_row = current_row[last_space_index + 1:]
                    y_row_counter += 10  # Zeilenhöhe
                    row_count += 1
                    last_space_index = -1 
                    if row_count >= max_rows:
                        break
            # Zeichne den Rest der letzten Zeile, wenn sie nicht vollständig war
            if current_row:
                can.imageblack.text(current_row, 5 + todo_x_cords[k], 20 + todo_y_cords[k] + y_row_counter, black)
            k=k+1
            if k>6:
                break
        
class BatteryLow(Tile):
    width = 800
    height = 480
    def draw_canvas(self, can):
        gc.collect()
        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)

        can.imagered.ellipse(self.x+400, self.y+240, 200, 200, red, True, )
        can.imagered.ellipse(self.x+400, self.y+240, 190, 190, 0x00, True)
        
        can.imagered.rect(self.x+275, self.y+180, 250, 120, red, True)
        can.imagered.rect(self.x+285, self.y+190, 230, 100, 0x00, True)
        
        can.imagered.rect(self.x+290, self.y+195, 40, 90, red, True)
        can.imagered.rect(self.x+335, self.y+195, 40, 90, red, False)
        can.imagered.rect(self.x+380, self.y+195, 40, 90, red, False)
        can.imagered.rect(self.x+380, self.y+195, 40, 90, red, False)
        can.imagered.rect(self.x+425, self.y+195, 40, 90, red, False)
        can.imagered.rect(self.x+470, self.y+195, 40, 90, red, False)
        
        can.imagered.rect(self.x+525, self.y+225, 10, 30, red, True)
    
        s=0
        for i in range(15):
            can.imagered.line(self.x+510+s, self.y+85, self.x+275+s, self.y+395, red)
            s=s+1

        can.imagered.text("Please replace the batteries!",self.x+290, self.y+460, red)

            
class NoConnection(Tile):
    gc.collect()
    width = 800
    height = 480
    def draw_canvas(self, can):
        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
      

        can.imagered.ellipse(self.x+400, self.y+240, 200, 200, red, True, )
        can.imagered.ellipse(self.x+400, self.y+240, 190, 190, 0x00, True)
        
        can.imagered.ellipse(self.x+400, self.y+290, 150, 150, red, True, 3)
        can.imagered.ellipse(self.x+400, self.y+290, 140, 140, 0x00, True)
        
        can.imagered.ellipse(self.x+400, self.y+290, 120, 120, red, True, 3)
        can.imagered.ellipse(self.x+400, self.y+290, 110, 110, 0x00, True)
        
        can.imagered.ellipse(self.x+400, self.y+290, 90, 90, red, True, 3)
        can.imagered.ellipse(self.x+400, self.y+290, 80, 80, 0x00, True)
        
        can.imagered.ellipse(self.x+400, self.y+290, 60, 60, red, True, 3)
        can.imagered.ellipse(self.x+400, self.y+290, 50, 50, 0x00, True)
        
        can.imagered.ellipse(self.x+400, self.y+290, 30, 30, red, True, )
        
        s=0
        for i in range(15):
            can.imagered.line(self.x+510+s, self.y+85, self.x+275+s, self.y+395, red)
            s=s+1
        
        can.imagered.text("Pleace check your WIFI connection and Config.py!",self.x+220, self.y+460, red)
        
         
