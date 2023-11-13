import time

from mss import mss as sct
import pyautogui as auto

#u = True
#while u == True:
    #r =auto.position()
    #print(r)
    #time.sleep(5)a
#img = cv2.imread('1.png')
#img = cv2.resize(img,(img.shape[1]//1, img.shape[0]//0.8))
#img = cv2.GaussianBlur(img,(3,3), 0)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#img = cv2.Canny(img,30,30)
#ker = np.ones((5,5), np.uint8)
#img = cv2.dilate(img,ker,iterations=1)
#img = cv2.erode(img,ker,iterations=1)
#cv2.imshow('', img)
#cv2.waitKey(0)
#pos = np.zeros((400,400,3),dtype='uint8')
#pos[:] = 0, 0, 200
#cv2.imshow('huita na ekrane',pos)
#cv2.waitKey(0)
#im = 'four.png'
#img = cv2.imread(im)
#def fc(event, x, y ,):
    #if event == 1:
       # y = input('y')
       # x = input('x')
      #  b,g,r = img[y,x]
       # print( r,g,b,)
       # event = 0
#cv2.imshow(img, fc(1, 22,34)))
z = None
while z == None:
      z = auto.locateOnScreen('four.png', confidence=0.5)
      auto.doubleClick(z)
      auto.doubleClick(z)
time.sleep(10)
for i in range(30):
     auto.scroll(-1000)
c = None
while c ==None:
    c =auto.locateOnScreen('five1.png', confidence=0.8)
    auto.click(c)
    auto.click(c)