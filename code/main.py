import driver
import tiles
from machine import Pin
import gc
import micropython
from picozero import Button

############################################################################
###          CUSTOMIZE LAYOUT HERE, TILES AT POSITION (X, Y)             ###
############################################################################

# Cycle throgh these tiles in the gallery using the next and previous Button
gallery = tiles.tile_gallery([
            #tiles.Weather_Tile_l(0,0),
            #tiles.ToDo_Tile(0,0),
            tiles.Calendar_Tile(0,0),
            tiles.News_Tile(0,0),
            ])

# Add static tiles that will be shown contiously
layout = [
            tiles.Clock_Tile_s(560, 0),
            tiles.Weather_Tile_s(560, 240),
            gallery,
         ]

############################################################################

update_flag = 0

# Button functions
def button_next():
    gallery.next_tile()
    global update_flag
    update_flag = 0
    print("next tile")

def button_prev():
    gallery.prev_tile()
    global update_flag
    update_flag = 0
    print("previous tile")

def button_ref():
    global update_flag
    update_flag = 0
    print("refresh screen")

# Main
if __name__=='__main__':
    gc.enable()
    gc.collect()
    
    # Init buttons
    btn_next = Button(3)                  # KEY1 GP3 pin 5
    btn_next.when_pressed = button_next
    btn_prev = Button(2)                  # KEY0 GP2 pin 4
    btn_prev.when_pressed = button_prev
    #btn_ref = Button(4)                  # GP4 pin 6
    #btn_next.when_pressed = button_ref
    
    # Initiate display object
    display = driver.EPD_7in5_B(layout)
    
    # Application Loop to refresh screen
    while True:
        update_flag = 60
        display.init()
        display.display()
        display.delay_ms(1000)
        display.sleep()
        display.delay_ms(1000)
        # Sleep for 1s, check if button was pressed
        while update_flag > 0:
            update_flag -= 1
            #machine.lightsleep(1000)  #use for Powersaving in Production
            time.sleep(1) 			  #use while debuging/ Development 
    