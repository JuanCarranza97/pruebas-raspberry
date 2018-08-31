from gpiozero import LED,Button
from time import sleep

led = LED(17)       #Led connected on pin 17
button = Button(22) #Button connected on pin 22

button.when_pressed = led.on
button.when_released = led.off

while True:
    print("Running ..")
    sleep(0.5)