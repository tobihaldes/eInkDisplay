import framebuf

# Parent class that defines Basic function for all tiles
class Tile():
    width = 100
    height = 100
    
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.canvas_black = framebuf.FrameBuffer(bytearray(self.height * self.width // 8), self.width, self.height, framebuf.MONO_HLSB)
        self.canvas_red = framebuf.FrameBuffer(bytearray(self.height * self.width // 8), self.width, self.height, framebuf.MONO_HLSB)
    def get_canvas_black(self):
        return self.canvas_black
        
    def get_canvas_red(self):
        return self.canvas_red
    
    """def move(self, x, y):
        self.y = y
        self.x = x"""
    
    
class Template_Tile(Tile):
    width = 200
    height = 200

    def get_canvas_black(self):
        can = self.canvas_black
        black = 0xff
        
        can.fill(0xff)
        can.rect(0, 0, self.width, self.height, black)

        return can

    def get_canvas_red(self):
        can = self.canvas_red
        red = 0xff
        
        can.fill(0x00)
        can.rect(0, 0, self.width, self.height, red)

        return can
    
class Wheather_Tile(Tile):
    width = 200
    height = 200

    def get_canvas_black(self):
        self.canvas_black.fill(0xff)
        self.canvas_black.rect(0, 0, 50, 50, 0x00, True)
        self.canvas_black.text("Wheather Tile!", 96, 100, 0x00)
        self.canvas_black.rect(0, 0, self.width, self.height, 0x00)

        return self.canvas_black

    def get_canvas_red(self):
        self.canvas_red.fill(0x00)
        self.canvas_red.rect(50, 50, 50, 50, 0xff, True)
        
        return self.canvas_red
    
    
class Calender_Tile(Tile):
    width = 200
    height = 200

    def get_canvas_black(self):
        self.canvas_black.fill(0xff)
        self.canvas_black.rect(50, 50, 50, 50, 0x00, True)
        self.canvas_black.rect(0, 0, self.width, self.height, 0x00)
        self.canvas_black.text("Calender Tile!", 96, 100, 0x00)

        return self.canvas_black

    def get_canvas_red(self):
        self.canvas_red.fill(0x00)
        self.canvas_red.rect(0, 0, 50, 50, 0xff, True)
        
        return self.canvas_red