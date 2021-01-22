import time
from pynput import keyboard
keyboardd = keyboard.Controller()
till = int(input("No of times: "))
text = input("text: ")
time.sleep(10)
while till >= 1:  # LOOP DE LOOP
    keyboardd.type(str(text))
    keyboardd.press(keyboard.Key.enter)
    keyboardd.release(keyboard.Key.enter)
    time.sleep(1.5)  # ADJUST ACCORDINGLY
    till -= 1
