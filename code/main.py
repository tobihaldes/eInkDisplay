import driver

if __name__=='__main__':
    epd = driver.EPD_7in5_B()
    epd.Clear()
    epd.imageblack.fill(0xff)
    epd.imagered.fill(0x00)

    epd.imageblack.text("Hello World", 5, 10, 0x00)
    epd.display()
    epd.delay_ms(10000)

    
    epd.Clear()
    epd.delay_ms(2000)
    epd.sleep()