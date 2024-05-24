import driver
import tiles
from machine import Pin
import gc
from picozero import Button
import time
#from config import layout_config, gallery_config
import config

update_flag = 0
led = Pin("LED", Pin.OUT)
led.toggle()

# Button functions
def button_next():
    led.toggle()
    gallery.next_tile()
    global update_flag
    update_flag = 0
    print("next tile")

def button_prev():
    led.toggle()
    gallery.prev_tile()
    global update_flag
    update_flag = 0
    print("previous tile")

def button_ref():
    led.toggle()
    global update_flag
    update_flag = 0
    print("refresh screen")

# Read tiles from config
def get_tile(tile_type, x, y):
    if tile_type == "Weather_Tile_l":
        return tiles.Weather_Tile_l(x, y)
    elif tile_type == "ToDo_Tile":
        return tiles.ToDo_Tile(x, y)
    elif tile_type == "Calendar_Tile":
        return tiles.Calendar_Tile(x, y)
    elif tile_type == "News_Tile":
        return tiles.News_Tile(x, y)
    elif tile_type == "Clock_Tile_s":
        return tiles.Clock_Tile_s(x, y)
    elif tile_type == "Weather_Tile_s":
        return tiles.Weather_Tile_s(x, y)
    else:
        raise ValueError(f"Unknown Tile-Typ (add customTiles to this function): {tile_type}")

# Main
if __name__=='__main__':
    led.toggle()
    gc.enable()
    gc.collect()
    
    # Initiate buttons
    btn_next = Button(3)                  # KEY1 GP3 pin 5
    btn_next.when_pressed = button_next
    btn_prev = Button(2)                  # KEY0 GP2 pin 4
    btn_prev.when_pressed = button_prev
    btn_ref = Button(4)                  # GP4 pin 6
    btn_ref.when_pressed = button_ref
    
    # Create tile_gallery from config
    gallery_tiles = [get_tile(tile["type"], tile["x"], tile["y"]) for tile in config.gallery_config]
    gallery = tiles.tile_gallery(gallery_tiles)

    # Create layout from config
    layout = [gallery]
    for item in config.layout_config:
        layout.append(get_tile(item["type"], item["x"], item["y"]))
    
    # Initiate display object
    display = driver.EPD_7in5_B(layout)
    
    # Refresh loop
    while True:
        gc.collect()
        update_flag = 60                 # Refresh every x seconds
        display.init()
        display.display()
        display.delay_ms(1000)
        display.sleep()
        display.delay_ms(1000)
        
        # Sleep for 1s, check if button was pressed
        while update_flag > 0:
            update_flag -= 1
            #machine.lightsleep(1000)     # Use for powersaving in production
            time.sleep(1)                # Use while debuging/ development 
    