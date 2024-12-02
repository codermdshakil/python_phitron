
# import pyautogui
import pyautogui

# take pyramid level
num = int(input())

# Draw the pyramid
for i in range(1, num + 1):
    pyautogui.typewrite("#" * i)   
    pyautogui.press("enter")      
