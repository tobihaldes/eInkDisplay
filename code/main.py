import driver
import tiles
from picozero import Button

def funcCall():
    print("pressed")
    
if __name__=='__main__':
    
    button = Button(18)
    button.when_pressed= funcCall
    
    dynTile = tiles.dynamic_Tile(300, 300, [
            tiles.Template_Tile(0,0),
            tiles.Calender_Tile(0,0),
            tiles.Weather_Tile(0,0),
            ])
    
    layout = [
        tiles.Weather_Tile(0,0),
        tiles.Calender_Tile(200,0),
        tiles.Template_Tile(0,200),
        dynTile,
        ]
    
    display = driver.EPD_7in5_B(layout)
    
    #display.Clear()
    display.imageblack.fill(0xff)
    display.imagered.fill(0x00)

    display.display()
    display.delay_ms(10000)
    
    dynTile.next_tile()
    display.display()
    display.delay_ms(10000)
    
    dynTile.next_tile()
    display.display()
    display.delay_ms(10000)
    
    dynTile.next_tile()
    display.display()
    display.delay_ms(10000)
    
    display.Clear()
    display.delay_ms(2000)
    display.sleep()