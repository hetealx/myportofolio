import pyautogui
import random
import time
time.sleep(2)
while True:
    x = random.randint (0,1500)
    y = random.randint (200,600)
    pyautogui.moveTo(x,y, 0.5)
    time.sleep(0.5)