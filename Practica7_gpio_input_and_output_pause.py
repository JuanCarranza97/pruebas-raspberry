from gpiozero import LED,Button
from signal import pause

led = LED(17)
button = Button(22)

print("Initializing..")
button.when_pressed = led.on
button.when_released = led.off
print("Done")

pause()