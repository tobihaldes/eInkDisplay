import driver
import tiles
from machine import Pin
#from picozero import Button

def button_next(pin):
    print("next tile")
    dynTile.next_tile()
    display.display()

def button_prev(pin):
    print("previous tile")
    dynTile.prev_tile()
    display.display()
   
if __name__=='__main__':
    
    #button = Button(4)
    #button.when_pressed= funcCall
    """
    button_next = Button(5) #KEY1 GP3 pin 5
    button_prev = Button(4)  #KEY0 GP2 pin 4
    button_next.when_pressed= button_next
    button_prev.when_pressed= button_prev
    """
    # Initialisierung Taster
    btn_next = Pin(3, Pin.IN, Pin.PULL_UP)
    btn_next.irq(trigger=Pin.IRQ_RISING, handler=button_next)
    btn_prev = Pin(2, Pin.IN, Pin.PULL_UP)
    btn_prev.irq(trigger=Pin.IRQ_RISING, handler=button_prev)

    # Taster-Auslösung
    
    
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
    display.delay_ms(120000)
    
    """
    dynTile.next_tile()
    display.display()
    display.delay_ms(10000)
    
    dynTile.next_tile()
    display.display()
    display.delay_ms(10000)
    
    dynTile.next_tile()
    display.display()
    display.delay_ms(10000)
    """
    
    display.Clear()
    display.delay_ms(2000)
    display.sleep()