import pyautogui
import time

def draw_pyramid(base_width):
    # Initial wait time to switch to the drawing application
    time.sleep(5)
    
    for i in range(1, base_width + 1):
        # For each level of the pyramid, calculate the number of characters
        text = '#' * i
        pyautogui.typewrite(text)
        # Move to the next line
        pyautogui.press('enter')
    
    # For a pause between drawing the two pyramids
    time.sleep(2)

# Drawing the first pyramid with a base width of 5
draw_pyramid(5)

# Drawi#ng the second pyramid with a base width of 1
draw_pyramid(1)
