from tiles import Tile
import framebuf


class Template_Tile(Tile):
    
    width = 240
    height = 240
    
    def draw_canvas(self, can):
           # ToDo: add example function draw rect, draw text, ...