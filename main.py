import random
import pyautogui as pt
import time

time.sleep(10)

pt.PAUSE = 0.3

aleatorio = random.randint(60, 180)

for i in range(20):
 time.sleep(aleatorio)
 pt.click(x=1837, y=530)

