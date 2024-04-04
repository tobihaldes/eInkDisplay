import driver
import tiles

if __name__=='__main__':
    
    display = driver.EPD_7in5_B()
    tile1 = tiles.Wheather_Tile(0,0)
    tile2 = tiles.Calender_Tile(200,0)
    tile3 = tiles.Template_Tile(0,200)
    
    display.Clear()
    display.imageblack.fill(0xff)
    display.imagered.fill(0x00)

    display.draw_Tile(tile1)
    display.draw_Tile(tile2)
    display.draw_Tile(tile3)
    display.display()
    display.delay_ms(10000)
    
    display.Clear()
    display.delay_ms(2000)
    display.sleep()
    
    """
    display = driver.EPD_7in5_B()
    
    display.imageblack.fill(0xff)
    display.imagered.fill(0x00)

    display.imageblack.text("Hello World", 5, 10, 0x00)
    display.imagered.text("Hello World", 5, 20, 0xff)
    display.display()
    display.delay_ms(15000)
    
    display.imageblack.rect(100, 100, 50, 50, 0x00, True)
    display.imagered.rect(115, 115, 20, 20, 0xff, True)
    display.display()
    display.delay_ms(15000)

    
    display.Clear()
    display.delay_ms(2000)
    display.sleep()
    """