from gpiozero import LED   #From gpiozero library import the LED function
from time import sleep     #From time library impor the sleep function


leds = [LED(17),LED(18)]

for x in range(5):
    leds[0].on()
    leds[1].off()
    sleep(.2)
    leds[0].off()
    leds[1].on()
    sleep(0.2)

