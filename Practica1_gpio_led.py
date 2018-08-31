from gpiozero import LED   #From gpiozero library import the LED function
from time import sleep     #From time library impor the sleep function

led_orange = LED(17)   ##Create a new LED object named led_orange at GPIO17 raspberry pin


for x in range(5):
    led_orange.on()
    sleep(.2)
    led_orange.off()
    sleep(0.2)

