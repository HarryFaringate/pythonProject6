import pyautogui as auto
import time
import numpy as np
import cv2
#im.save('1.png')
u = True
while u == True:
    r =auto.position()
    print(r)
    time.sleep(5)


#r = auto.screenshot()
#lsr.save('seven.png')
#z = None
#while z == None:
      #z = auto.locateOnScreen('four.png', confidence=0.5)
      #auto.click(z)
#auto.click(r)
#time.sleep(3)
#ax = auto.screenshot(region=(380,155,390,165))
#ax.save('four.png')

#ax = cv2.imread('four.png')
#ax = cv2.cvtColor(ax, cv2.COLOR_BGR2v2.setMouseCallBack()RGB)
#ax = cv2.Canny(ax,30,30)
#ker = np.ones((5,5), np.uint8)
#ax= cv2.dilate(ax,ker,iterations=1)
#ax = cv2.erode(ax,ker,iterations=1)
#x = auto.locateOnScreen('four.png', confidence=0.5)
#auto.click(x)
#x = tesseract.image_to_string(ax)
#cv2.imshow(x)
#cv2.waitKey(0)
#x=193, y=130 x=280, y=209
#x=21, y=611x=565, y=700)
#1157, y=204x=1022, y=98