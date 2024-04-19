import framebuf

black = 0x00
red = 0xff
white = 0x00

# Parent class that defines Basic function for all tiles
class Tile():
    width = 100
    height = 100
    
    def __init__(self, x, y):
        self.y = y
        self.x = x
        
    def draw_canvas(self, can):
        print("a")
        can.imagered.fill(0x00)
        can.imageblack.fill(0xff)
        
    
    """def move(self, x, y):
        self.y = y
        self.x = x"""
    
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
        self.tiles[self.current_index].draw_canvas(can)


class Template_Tile(Tile):
    width = 400
    height = 400

    def draw_canvas(self, can):
        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
      
class Clock_Tile_s(Tile):
    width = 240
    height = 240
    
    def draw_canvas(self, can):
        i = 1
        #Parameter für Stunden und Minuten
        timeHour = 22
        minuteQuarter = 1

        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
        
        #Stundenzahlen
        if timeHour == 1:
            #Z1oben
            can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
            #Z1links oben
            can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1links unten
            can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            #Z1unten
            can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
            
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
        elif timeHour == 2:
            #Z1oben
            can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
            #Z1links oben
            can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1links unten
            can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            #Z1unten
            can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2links unten
            can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
            #Z2unten
            can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
        elif timeHour == 3:
            #Z1oben
            can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
            #Z1links oben
            can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1links unten
            can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            #Z1unten
            can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2links unten
            can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
            #Z2unten
            can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
        elif timeHour == 4:
            #Z1oben
            can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
            #Z1links oben
            can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1links unten
            can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            #Z1unten
            can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2links oben
            can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
        elif timeHour == 5:
            #Z1oben
            can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
            #Z1links oben
            can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1links unten
            can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            #Z1unten
            can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
             #Z2links oben
            can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
            #Z2unten
            can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
        elif timeHour == 6:
            #Z1oben
            can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
            #Z1links oben
            can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1links unten
            can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            #Z1unten
            can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2links oben
            can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2links unten
            can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
            #Z2unten
            can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
        elif timeHour == 7:
            #Z1oben
            can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
            #Z1links oben
            can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1links unten
            can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            #Z1unten
            can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
        elif timeHour == 8:
            #Z1oben
            can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
            #Z1links oben
            can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1links unten
            can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            #Z1unten
            can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2unten
            can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
            #Z2links oben
            can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2links unten
            can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)  
        elif timeHour == 9:
            #Z1oben
            can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
            #Z1links oben
            can.imageblack.rect(self.x+85, self.y+87, 6, 36, black, True)
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1links unten
            can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            #Z1unten
            can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2unten
            can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
            #Z2links oben
            can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)  
        elif timeHour == 10:
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2unten
            can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
            #Z2links oben
            can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2links unten
            can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True) 
        elif timeHour == 11:
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True) 
        elif timeHour == 12:
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2links unten
            can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
            #Z2unten
            can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
        elif timeHour == 13:
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2links unten
            can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
            #Z2unten
            can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
        elif timeHour == 14:
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2links oben
            can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
        elif timeHour == 15:
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
             #Z2links oben
            can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
            #Z2unten
            can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
        elif timeHour == 16:
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2links oben
            can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2links unten
            can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
            #Z2unten
            can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
        elif timeHour == 17:
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
        elif timeHour == 18:
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2unten
            can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
            #Z2links oben
            can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2links unten
            can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)  
        elif timeHour == 19:
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1rechts unten
            can.imageblack.rect(self.x+109, self.y+117, 6, 36, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2unten
            can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
            #Z2links oben
            can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)  
        elif timeHour == 20:
            #Z1oben
            can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1mitte
            can.imageblack.rect(self.x+85, self.y+117, 30, 6, black, True)
            #Z1links unten
            can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
            #Z1unten
            can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2unten
            can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
            #Z2links oben
            can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2links unten
            can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True) 
        elif timeHour == 21:
            #Z1oben
            can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1mitte
            can.imageblack.rect(self.x+85, self.y+117, 30, 6, black, True)
            #Z1links unten
            can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
            #Z1unten
            can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
            
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
        elif timeHour == 22:
            #Z1oben
            can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1mitte
            can.imageblack.rect(self.x+85, self.y+117, 30, 6, black, True)
            #Z1links unten
            can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
            #Z1unten
            can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2links unten
            can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
            #Z2unten
            can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
        elif timeHour == 23:
            #Z1oben
            can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1mitte
            can.imageblack.rect(self.x+85, self.y+117, 30, 6, black, True)
            #Z1links unten
            can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
            #Z1unten
            can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2links unten
            can.imageblack.rect(self.x+125, self.y+117, 6, 36, black, True)
            #Z2unten
            can.imageblack.rect(self.x+125, self.y+147, 30, 6, black, True)
        elif timeHour == 24:
            #Z1oben
            can.imageblack.rect(self.x+85, self.y+87, 30, 6, black, True)
            #Z1rechts oben
            can.imageblack.rect(self.x+109, self.y+87, 6, 36, black, True)
            #Z1mitte
            can.imageblack.rect(self.x+85, self.y+117, 30, 6, black, True)
            #Z1links unten
            can.imageblack.rect(self.x+85, self.y+117, 6, 36, black, True)
            #Z1unten
            can.imageblack.rect(self.x+85, self.y+147, 30, 6, black, True)
            
            #Z2oben
            can.imageblack.rect(self.x+125, self.y+87, 30, 6, black, True)
            #Z2links oben
            can.imageblack.rect(self.x+125, self.y+87, 6, 36, black, True)
            #Z2rechts oben
            can.imageblack.rect(self.x+149, self.y+87, 6, 36, black, True)
            #Z2mitte
            can.imageblack.rect(self.x+125, self.y+117, 30, 6, black, True)
            #Z2rechts unten
            can.imageblack.rect(self.x+149, self.y+117, 6, 36, black, True)
            
        #Viertelstunden Zeiger 
        if minuteQuarter == 1:
            for x in range(0, 7):
                can.imagered.ellipse(self.x+120, self.y+120, 100+i, 100+i, red, False, 1)
                i = i+1
        elif minuteQuarter ==2:
            for x in range(0, 7):
                can.imagered.ellipse(self.x+120, self.y+120, 100+i, 100+i, red, False, 9)
                i = i+1
        elif minuteQuarter ==3:
            for x in range(0, 7):
                can.imagered.ellipse(self.x+120, self.y+120, 100+i, 100+i, red, False, 13)
                i = i+1
        elif minuteQuarter ==4:
            for x in range(0, 7):
                can.imagered.ellipse(self.x+120, self.y+120, 100+i, 100+i, red, False, 15)
                i = i+1
        can.imageblack.ellipse(self.x+120, self.y+120, 108, 108, black)
        can.imageblack.ellipse(self.x+120, self.y+120, 100, 100, black)
        #Ziffernblatt oben und unten
        can.imageblack.rect(self.x+118, self.y+25, 4, 20, black, True)
        can.imageblack.rect(self.x+118, self.y+195, 4, 20, black, True)
        #Ziffernblatt links und rechts
        can.imageblack.rect(self.x+25, self.y+118, 20, 4, black, True)
        can.imageblack.rect(self.x+195, self.y+118, 20, 4, black, True)
        #Ziffernblatt kleine Striche
        can.imageblack.line(self.x+171-5, self.y+33+5, self.x+158, self.y+53, black)
        can.imageblack.line(self.x+208-5, self.y+69+5, self.x+186, self.y+82, black)
        can.imageblack.line(self.x+208-5, self.y+171-5, self.x+186, self.y+158, black)
        can.imageblack.line(self.x+171-5, self.y+208-5, self.x+158, self.y+186, black)
        can.imageblack.line(self.x+69+5, self.y+208-5, self.x+82, self.y+186, black)
        can.imageblack.line(self.x+33+5, self.y+171-5, self.x+53, self.y+158, black)
        can.imageblack.line(self.x+33+5, self.y+69+5, self.x+53, self.y+82, black)
        can.imageblack.line(self.x+69+5, self.y+33+5, self.x+82, self.y+53, black)
        
        #mitte der Uhr
        can.imageblack.pixel(self.x+120, self.y+120, black)
        
        
        
        
    
    
    
class Weather_Tile_s(Tile):
    width = 240
    height = 240
    
    def draw_canvas(self, can):
        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
        can.imageblack.text("Datum: Heute", self.x+70, self.y+15, black)
        
    
class Weather_Tile_l(Tile):
    width = 560
    height = 480
    
    def draw_canvas(self, can):
        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
        
        #Gitternetzlinien
        #Horizontal
        can.imageblack.rect(self.x+10, self.y+240, 540, 2, black, True)
        #Vertikal oben
        can.imageblack.rect(self.x+186, self.y+10, 2, 220, black, True)
        can.imageblack.rect(self.x+373, self.y+10, 2, 220, black, True)
        #vertikal unten
        can.imageblack.rect(self.x+186, self.y+250, 2, 220, black, True)
        can.imageblack.rect(self.x+373, self.y+250, 2, 220, black, True)
        
        #Datum oben
        can.imageblack.text("Datum: tt.mm.jjjj", self.x+25, self.y+15, black)
        can.imageblack.text("Datum: tt.mm.jjjj", self.x+212, self.y+15, black)
        can.imageblack.text("Datum: tt.mm.jjjj", self.x+399, self.y+15, black)
        #Datum unten
        can.imageblack.text("Datum: tt.mm.jjjj", self.x+25, self.y+255, black)
        can.imageblack.text("Datum: tt.mm.jjjj", self.x+212, self.y+255, black)
        can.imageblack.text("Datum: tt.mm.jjjj", self.x+399, self.y+255, black)
        
        
    
# class Calender_Tile(Tile):
#     width = 200
#     height = 200
#     
#     def draw_canvas(self, can):
#         can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
#         can.imageblack.rect(self.x+50, self.y+50, 50, 50, black, True)
#         can.imagered.rect(self.x+0, self.y+0, 50, 50, red, True)
#         can.imageblack.text("Calender Tile!", self.x+96, self.y+100, black)