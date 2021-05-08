import time
from pynput import keyboard

keyboardd = keyboard.Controller()
i = 1
time.sleep(10)  #  TIME TILL GO TO APP  #

while True:  #  LOOP DE LOOP  #
    keyboardd.type(str(i))
    keyboardd.press(keyboard.Key.enter)
    keyboardd.release(keyboard.Key.enter)
    time.sleep(1.4)  # ADJUST ACCORDINGLY  #
    i += 1
