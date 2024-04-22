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
            can.imagered.ellipse(self.x+120, self.y+120, 107, 107, red, True, 1)
        elif minuteQuarter ==2:
            can.imagered.ellipse(self.x+120, self.y+120, 107, 107, red, True, 9)
        elif minuteQuarter ==3:
            can.imagered.ellipse(self.x+120, self.y+120, 107, 107, red, True, 13)
        elif minuteQuarter ==4:
            can.imagered.ellipse(self.x+120, self.y+120, 107, 107, red, True, 15)
                
        can.imageblack.ellipse(self.x+120, self.y+120, 108, 108, black, False)
        can.imageblack.ellipse(self.x+120, self.y+120, 100, 100, black)
        can.imagered.ellipse(self.x+120, self.y+120, 100, 100, 0x00, True)
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
    
class Weather_Tile_s(Tile):
    width = 240
    height = 240
    
    def draw_canvas(self, can):
        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
        can.imageblack.text("Datum: Heute", self.x+70, self.y+16, black)
        can.imagered.text("Max Temperatur: 22", self.x+45, self.y+211, red)
        can.imageblack.text("Min Temperatur: 12", self.x+45, self.y+226, black)
        can.imageblack.rect(self.x+70, self.y+41, 100, 100, black, False)
    
        y_row_counter = 0
        row_count = 0
        max_rows = 4
        cols = 210 // 8 #Breite des Textfeldes
        current_row = ''
        last_space_index = -1  
        text = "Das ist eine ganz lange Beschreibung fuer das heutige Wetter."
        
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
    
    def draw_canvas(self, can):
        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
        #Gitternetzlinien Horizontal
        can.imageblack.rect(self.x+10, self.y+240, 540, 2, black, True)
        
        weather_x_cords = [0, 187, 374, 0, 187, 374]
        weather_y_cords = [0, 0, 0, 242, 242, 242]
        weather_dates = ["Datum: 01.mm.jjjj", "Datum: 02.mm.jjjj", "Datum: 03.mm.jjjj", "Datum: 04.mm.jjjj", "Datum: 05.mm.jjjj", "Datum: 06.mm.jjjj",]
        temp_high = [21, 22, 23, 22, 26, 27]
        temp_low = [18, 16, 18, 19, 20, 18]
        weather_status = ["Das ist ein Wetter Status 1", "Das ist ein Wetter Status 2", "Das ist ein Wetter Status 3", "Das ist ein Wetter Status 4", "Das ist ein Wetter Status 5", "Das ist ein Wetter Status 6"]
        weather_icon = [1, 2, 3, 2, 3, 1]
        k=0
        for i in range(6):
            can.imageblack.rect(self.x+weather_x_cords[k]-2, self.y+weather_y_cords[k]+10, 2, 220, black, True)
            can.imageblack.text(weather_dates[k], self.x+weather_x_cords[k]+25, self.y+weather_y_cords[k]+15, black)
            can.imagered.text("Max Temperatur: "+str(temp_high[k]), self.x+weather_x_cords[k]+25, self.y+weather_y_cords[k]+210, red)
            can.imageblack.text("Min Temperatur: "+str(temp_low[k]), self.x+weather_x_cords[k]+25, self.y+weather_y_cords[k]+225, black)
            
            y_row_counter = 0
            row_count = 0
            max_rows = 4
            cols = 170 // 8 #Breite des Textfeldes
            current_row = ''
            last_space_index = -1  
            text = weather_status[k]
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
            #Weathe Icon
            if weather_icon[k]==1:
                can.imageblack.rect(self.x+weather_x_cords[k]+43, self.y+weather_y_cords[k]+40, 100, 100, black, False)
                can.imagered.text("Icon 1 POC", self.x+weather_x_cords[k]+43, self.y+weather_y_cords[k]+80, red)
            elif weather_icon[k]==2:
                can.imageblack.rect(self.x+weather_x_cords[k]+43, self.y+weather_y_cords[k]+40, 100, 100, black, False)
                can.imagered.text("Icon 2 POC", self.x+weather_x_cords[k]+43, self.y+weather_y_cords[k]+80, red)
            elif weather_icon[k]==3:
                can.imagered.rect(self.x+weather_x_cords[k]+43, self.y+weather_y_cords[k]+40, 100, 100, red, False)
                can.imageblack.text("Icon 3 POC", self.x+weather_x_cords[k]+43, self.y+weather_y_cords[k]+80, black)
            k=k+1
    
class ToDo_Tile(Tile):
    width = 560
    height = 480
    def draw_canvas(self, can):
        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
        todo_x_cords = [5, 190, 375, 5, 190, 375, 5, 190, 375, 5, 190, 375]
        todo_y_cords = [5, 5, 5, 120, 120, 120, 235, 235, 235, 350, 350, 350]
        todo_data = [["Aufgabe: Hausaufgaben fuer die UNI erledigen", "Faellig am xx.xx.xx"], ["Aufgabe: Das Zimmer aufraeumen", "Faellig am xx.xx.xx"], ["Aufgabe: Smart Display programmieren und dann in Git hochladen, damit alle den Code haben.", "Faellig am xx.xx.xx"], ["Aufgabe: Weitere Sachen die gemacht werden muessen.", "Faellig am xx.xx.xx"], ["Aufgabe: Weitere Sachen die gemacht werden muessen.", "Faellig am xx.xx.xx"], ["Aufgabe: Weitere Sachen die gemacht werden muessen.", "Faellig am xx.xx.xx"], ["Aufgabe: Weitere Sachen die gemacht werden muessen.", "Faellig am xx.xx.xx"], ["Aufgabe: Weitere Sachen die gemacht werden muessen.", "Faellig am xx.xx.xx"], ["Aufgabe: Weitere Sachen die gemacht werden muessen.", "Faellig am xx.xx.xx"], ["Aufgabe: Weitere Sachen die gemacht werden muessen.", "Faellig am xx.xx.xx"], ["Aufgabe: Weitere Sachen die gemacht werden muessen.", "Faellig am xx.xx.xx"]]
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
            text = todo_data[k][0] 
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
        
        
        