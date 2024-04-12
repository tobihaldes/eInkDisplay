import driver

if __name__=='__main__':
    epd = driver.EPD_7in5_B()
    epd.Clear()
    
    epd.imageblack.fill(0xff)
    epd.imagered.fill(0x00)
    
    epd.imageblack.text("Waveshare", 5, 10, 0x00)
    epd.imagered.text("Pico_ePaper-7.5-B", 5, 40, 0xff)
    epd.imageblack.text("Raspberry Pico", 5, 70, 0x00)
    epd.display()
    epd.delay_ms(5000)
    
    epd.imageblack.vline(10, 90, 60, 0x00)
    epd.imageblack.vline(120, 90, 60, 0x00)
    epd.imagered.hline(10, 90, 110, 0xff)
    epd.imagered.hline(10, 150, 110, 0xff)
    epd.imagered.line(10, 90, 120, 150, 0xff)
    epd.imagered.line(120, 90, 10, 150, 0xff)
    epd.display()
    epd.delay_ms(5000)
    
    epd.imageblack.rect(10, 180, 50, 80, 0x00 )
    epd.imageblack.fill_rect(70, 180, 50, 80,0x00 )
    epd.imagered.rect(10, 300, 50, 80, 0xff )
    epd.imagered.fill_rect(70, 300, 50, 80,0xff )
    epd.display()
    epd.delay_ms(5000)

    for k in range(0, 3):
        for j in range(0, 3):
            for i in range(0, 5):
                epd.imageblack.fill_rect(200+100+j*200, i*20+k*200, 100, 10, 0x00)
            for i in range(0, 5):
                epd.imagered.fill_rect(200+0+j*200, i*20+100+k*200, 100, 10, 0xff)
    epd.display()
    epd.delay_ms(5000)

    epd.Clear()
    epd.delay_ms(2000)
    print("sleep")
    epd.sleep()