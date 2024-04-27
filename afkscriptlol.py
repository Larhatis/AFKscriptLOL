import pyautogui
import time
import random

while True:
    pyautogui.click(x=pyautogui.size().width - 100, y=pyautogui.size().height // 2)
    time.sleep(5)

    
    pyautogui.click(x=100, y=pyautogui.size().height // 2)
    time.sleep(5)

    pyautogui.hotkey(random.choice(['z', 'a', 'e']))
    time.sleep(5)
