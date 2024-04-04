import framebuf

# Parent class that defines Basic function for all tiles
class Tile():
    width = 100
    height = 100
    
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.canvas_black = framebuf.FrameBuffer([], self.width, self.height, framebuf.MONO_HLSB)
        self.canvas_red = framebuf.FrameBuffer([], self.width, self.height, framebuf.MONO_HLSB)

    def get_canvas_black(self):
        return self.canvas_black
        
    def get_canvas_red(self):
        return self.canvas_red
    
    """def move(self, x, y):
        self.y = y
        self.x = x"""
    
class Wheather_Tile(Tile):
    width = 200
    height = 200

    def get_canvas_black(self):
        self.canvas_black.rect(0, 0, 50, 50, 0xff)

        return self.canvas_black

    def get_canvas_red(self):
        self.canvas_black.rect(50, 50, 50, 50, 0xff)

        return self.canvas_red