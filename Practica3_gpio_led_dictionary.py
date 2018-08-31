from gpiozero import LED
from time import sleep

leds={'led1':LED(17),'led2':LED(18)}

while True:
    leds['led1'].on()
    leds['led2'].off()
    sleep(0.2)
    leds['led1'].off()
    leds['led2'].on()
    sleep(0.2)