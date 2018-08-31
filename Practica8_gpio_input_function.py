from gpiozero import Button
from signal import pause

def button_function():
    print("Button pressed")

button = Button(22)

button.when_pressed = button_function
print("Ready :)")

pause()

