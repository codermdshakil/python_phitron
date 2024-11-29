
import pyautogui
from time import sleep

print("Hello world")
sleep(5)
for i in range(0,10):
    pyautogui.write("I love Programming and Now Python!", interval=0.25) 
    pyautogui.press('enter')

 
# pip install pyautogui