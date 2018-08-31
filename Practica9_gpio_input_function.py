from gpiozero import LED,Button
from signal import pause

def button_function():
    print("Button pressed")
    led.on()

button = Button(22)
led = LED(17)

button.when_pressed = button_function
button.when_released = led.off
print("Ready :)")

pause()

