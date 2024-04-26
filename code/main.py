import driver
import tiles
from machine import Pin
import gc
import micropython
from picozero import Button

update_flag = 0

def button_next(pin):
    print("next tile")
    gallery.next_tile()
    update_flag = 0

def button_prev(pin):
    print("previous tile")
    gallery.prev_tile()
    update_flag = 0
    
if __name__=='__main__':
    gc.enable()
    gc.collect()
    
    # Initialisierung Taster
    """
    btn_next = Pin(3, Pin.IN, Pin.PULL_UP)  #KEY1 GP3 pin 5
    btn_next.irq(trigger=Pin.IRQ_RISING, handler=button_next)
    btn_prev = Pin(2, Pin.IN, Pin.PULL_UP)    #KEY0 GP2 pin 4
    btn_prev.irq(trigger=Pin.IRQ_RISING, handler=button_prev)
    """
    
    btn_next = Button(3)
    btn_next.when_pressed = button_next
    btn_prev = Button(2)
    btn_prev.when_pressed = button_prev
    
    # Layout
    gallery = tiles.tile_gallery([
            tiles.Weather_Tile_l(0,0),
            tiles.ToDo_Tile(0,0),
            tiles.Calendar_Tile(0,0),
            tiles.News_Tile(0,0),
            ])
    
    layout = [
        tiles.Clock_Tile_s(560, 0),
        tiles.Weather_Tile_s(560, 240),
        gallery,
        ]
    
    # initiate Display Objekt
    display = driver.EPD_7in5_B(layout)
    #micropython.mem_info(1)
    
    while True:
        update_flag = 60
        display.init()
        display.display()
        display.delay_ms(1000)
        display.sleep()
        display.delay_ms(1000)
        while 0 < update_flag:
            update_flag -= 1
            machine.lightsleep(1000)
            
    
    
    display.Clear()
    display.delay_ms(2000)
    display.sleep()