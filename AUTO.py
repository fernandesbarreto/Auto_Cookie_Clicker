import pyautogui
from time import sleep

pyautogui.PAUSE = 0.01
cont = 0
while True:
    for c in range(0, 5000):
        cont += 1
        pyautogui.click(309, 536)
        print(cont)
    for c in range(0):
        pyautogui.click(1089, 301)
    for c in range (0, 50):
        pyautogui.click(1203, 480)
    sleep(3)
    cont = 0
