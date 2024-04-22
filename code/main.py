import driver
import tiles
from machine import Pin
import gc
#from picozero import Button

def button_next(pin):
    print("next tile")
    gallery.next_tile()
    display.display()

def button_prev(pin):
    print("previous tile")
    gallery.prev_tile()
    display.display()
   
if __name__=='__main__':
    gc.enable()
    # Initialisierung Taster
    btn_next = Pin(3, Pin.IN, Pin.PULL_UP)  #KEY1 GP3 pin 5
    btn_next.irq(trigger=Pin.IRQ_RISING, handler=button_next)
    btn_prev = Pin(2, Pin.IN, Pin.PULL_UP)    #KEY0 GP2 pin 4
    btn_prev.irq(trigger=Pin.IRQ_RISING, handler=button_prev)
    
    # Layout
    gallery = tiles.tile_gallery([
#             tiles.Template_Tile(0,0),
#             tiles.Calender_Tile(0,0),
             tiles.Weather_Tile_l(0,0),
             tiles.Weather_Tile_s(0,0),
            ])
    
    layout = [
        #tiles.Weather_Tile_l(0, 0),
        tiles.Clock_Tile_s(560, 0),
        tiles.Weather_Tile_s(560, 240),
        #tiles.Calender_Tile(200, 0),
        #tiles.Template_Tile(400, 0),
        #tiles.Template_Tile(0,200),
        gallery,
        ]
    
    # initiate Display Objekt
    display = driver.EPD_7in5_B(layout)
    
    #display.Clear()
    display.imagered.fill(0x00)
    display.imageblack.fill(0xff)
    

    while True:
        display.init()
        display.display()
        display.delay_ms(1000)
        display.sleep()
        display.delay_ms(1000)
        machine.lightsleep(60000)
    
    
    display.Clear()
    display.delay_ms(2000)
    display.sleep()