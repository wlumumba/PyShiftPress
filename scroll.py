import pyautogui
import time

while True:
    time.sleep(10)
    """ #if you wanted mouse movement instead!
    for i in range(1, 144, 4):
        pyautogui.moveTo(960, i * 4)
    """
    pyautogui.press('shift')
    print("Shift button pressed at {}".format(time.strftime('%I:%M:%S')))

    