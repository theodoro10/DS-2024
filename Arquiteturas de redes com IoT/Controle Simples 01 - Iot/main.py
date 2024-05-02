import machine                                                                                                                                                
from machine import Pin, I2C
import ssd1306

i2c = I2C(0, scl=Pin(21), sda=Pin(5))
led = machine.Pin(32, machine.Pin.OUT)
led2 = machine.Pin(25, machine.Pin.OUT)
botao = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
botao2 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)



largura = 128
altura = 64

tela = ssd1306.SSD1306_I2C(largura, altura, i2c)
while True: 
    blue = botao.value()
    red = botao2.value()

    if blue == 0:
        tela.fill(0)
        tela.text("Corinthians 2012", 0, 0)
        tela.text("Corinthians 2013", 0, 10)
        tela.text("Corinthians 2002", 0, 20)
        tela.show()
        led.value(1)
        led2.value(0)
        
        
   
    if red == 0:
         tela.fill(0)
         tela.text("Craque Neto", 0, 0)
         tela.text("Cassio", 0, 10)
         tela.text("Rivelino", 0, 20)
         tela.show() 
         led2.value(1)
         led.value(0)
         
         
    
