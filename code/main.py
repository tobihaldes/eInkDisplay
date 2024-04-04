import driver
import tiles

if __name__=='__main__':
    display = driver.EPD_7in5_B()
    display.Clear()
    display.imageblack.fill(0xff)
    display.imagered.fill(0x00)

    display.imageblack.text("Hello World", 5, 10, 0x00)
    display.display()
    display.delay_ms(10000)

    
    display.Clear()
    display.delay_ms(2000)
    display.sleep()

    """
    display = driver.EPD_7in5_B()
    tile1 = tiles.Wheather_Tile(0,0)
    display.Clear()
    display.imageblack.fill(0xff)
    display.imagered.fill(0x00)

    display.draw_Tile(tile1)
    display.display()
    display.delay_ms(10000)

    
    display.Clear()
    display.delay_ms(2000)
    display.sleep()
    """