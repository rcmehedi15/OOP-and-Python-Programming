import pyautogui
import time

def draw_pyramid(height):
    for i in range(height):
        line = '#' * (i + 1)
        pyautogui.typewrite(line)
        pyautogui.press('enter')

print("You have 5 seconds to switch to the window where you want to draw the pyramid...")
time.sleep(5)

height = int(input("Enter the height of the pyramid: "))
draw_pyramid(height)
