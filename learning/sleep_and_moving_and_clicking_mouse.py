import pyautogui
import time


#waits 5 seconds
time.sleep(5)

#prints the size of the screen
print(pyautogui.size())

#prints the mouse position
print(pyautogui.position())

#moves mouse to the x and y coordinates occording to the screen size
pyautogui.moveTo(2120, 700)

#makes the mouse click
pyautogui.click()