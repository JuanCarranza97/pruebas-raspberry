from gpiozero import Button

pinButton = 22

button = Button(pinButton)

print("Press button {} to continue".format(pinButton))
button.wait_for_press()
print("The button was pressed")