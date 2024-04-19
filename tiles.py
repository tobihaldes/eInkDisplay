import framebuf


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
        print("a")
        can.imageblack.fill(0xff)
        can.imagered.fill(0x00)
    
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
        
    
class Weather_Tile_s(Tile):
    width = 240
    height = 240
    
    def draw_canvas(self, can):
        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
        #can.imageblack.rect(self.x+0, self.y+0, 50, 50, black, True)
        can.imagered.rect(self.x+50, self.y+50, 50, 50, red, True)
        can.imageblack.text("Weather Tile small!", self.x+96, self.y+100, black)
    
class Weather_Tile_l(Tile):
    width = 560
    height = 480
    
    def draw_canvas(self, can):
        can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
        can.imageblack.rect(self.x+0, self.y+0, 50, 50, black, True)
        can.imagered.rect(self.x+50, self.y+50, 50, 50, red, True)
        can.imageblack.text("Weather Tile large!", 96, 100, black)
    
# class Calender_Tile(Tile):
#     width = 200
#     height = 200
#     
#     def draw_canvas(self, can):
#         can.imageblack.rect(self.x+0, self.y+0, self.width, self.height, black)
#         can.imageblack.rect(self.x+50, self.y+50, 50, 50, black, True)
#         can.imagered.rect(self.x+0, self.y+0, 50, 50, red, True)
#         can.imageblack.text("Calender Tile!", self.x+96, self.y+100, black)