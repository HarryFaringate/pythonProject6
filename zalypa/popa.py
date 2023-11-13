import pyautogui as auto
import time
import cv2
time.sleep(5)
c = None
while c ==None:
    c = auto.locateOnScreen('five1.png', confidence=0.5)
    auto.click(c)
    auto.click(c)
