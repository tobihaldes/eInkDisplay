import driver
import tiles
from machine import Pin
import gc
import micropython
from picozero import Button
from config import layout, gallery

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
    
    # Initiate buttons
    btn_next = Button(3)                  # KEY1 GP3 pin 5
    btn_next.when_pressed = button_next
    btn_prev = Button(2)                  # KEY0 GP2 pin 4
    btn_prev.when_pressed = button_prev
    #btn_ref = Button(4)                  # GP4 pin 6
    #btn_next.when_pressed = button_ref
    
    # Initiate display object
    display = driver.EPD_7in5_B(layout)
    
    # Refresh loop
    while True:
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
    