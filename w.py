import pyautogui
import time
time.sleep(5)
i=0

while i<=20:
    pyautogui.typewrite(f"")
    pyautogui.press("enter")
    time.sleep(1)

    i+=1