import time
import pyautogui
import os
import cv2

def is_not_zero(expected_image):
    '''
    this function will return a true val if there is the image and false if not
    :param screenshot:
    :param expected_image:
    :return: bool or tuple(condensates)
    '''


    time.sleep(5)

    while True:

        try:

            x, y, z, k = pyautogui.locateOnScreen(expected_image + '.png')
            return True

        except:

             return False


pyautogui.FAILSAFE = True # disables the fail-safe
pyautogui.position()
condition = True

while condition:
    x, y = pyautogui.locateCenterOnScreen('click.png')
    time.sleep(5)
    pyautogui.click(x, y)
    time.sleep(5)

    x, y = pyautogui.locateCenterOnScreen('click2.png')
    time.sleep(5)
    pyautogui.click(x, y)
    time.sleep(5)
    if is_not_zero('Capture1'):
        #send email
        break
    else:
        x, y = pyautogui.locateCenterOnScreen('back.png')
        time.sleep(5)
        pyautogui.click(x, y)
        time.sleep(5)