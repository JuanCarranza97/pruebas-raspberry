from gpiozero import Button
from signal import pause
import sys

def button_up_pressed():
    global x
    x+=1
    print("El valor de x es {}".format(x))
  
def button_down_pressed():
    global x
    x-=1
    print("El valor de x es {}".format(x))
    
x = 0

button_up = Button(22)
button_down = Button(23)

button_up.when_pressed = button_up_pressed
button_down.when_pressed = button_down_pressed

pause()
    
    