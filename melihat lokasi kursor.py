#melihat lokasi kursor
import pyautogui
import time

while True:
    x, y = pyautogui.position()
    print(f"X={x}, Y={y}")
