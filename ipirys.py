import time
import keyword as kb
import pyautogui as auto
import cv2
def bying ():
    a = True
    x = 500
    y = 300
    gr = (0, 255, 0)
    while a == True:
        try:
            r = auto.pixelMatchesColor(x,y,(0, 255, 0),tolerance=50)
            while r ==True:
               z = x + 50
               auto.click(z,y)
               r = auto.pixelMatchesColor(x, y, (0, 255, 0), tolerance=50)
            else:
               x = x +1
               y = y +1
               if x>=520:
                   x = x -10
        except OSError:
            auto.scroll(-550)
            return
def sale ():
    a = True
    x = 1841
    y = 200
    gr = (0, 255, 0)
    while a == True:
        try:
            r = auto.pixelMatchesColor(x, y, (0, 255, 0), tolerance=50)
            while r == True:
                z = x - 480
                auto.click(z, y)
                r = auto.pixelMatchesColor(x, y, (0, 255, 0), tolerance=50)
            else:
                x = x + 1
                y = y + 1
                if x >= 1860:
                    x = x - 15
        except OSError:
            auto.scroll(-550)
            return
def loc0():
   i = None
   while i ==None:
       i = auto.locateOnScreen('one.png', confidence=0.7)
       auto.click(i)
       auto.click(i)
def loc1():
    x = None
    while x == None:
        x = auto.locateOnScreen('two.png', confidence=0.7)
        auto.click(x)
        auto.click(x)
        print(x)

def loc2():
    y = None
    while y == None:
        y = auto.locateOnScreen('three.png', confidence=0.9)
        auto.click(y)
        auto.click(y)
def loc3():
   z = None
   while z == None:
      z = auto.locateOnScreen('four.png', confidence=0.5)
      auto.click(z)
      auto.click(z)

def nai():
    c = None
    while c == None:
        c = auto.locateOnScreen('five3.png', confidence=0.7)
        auto.click(c)
        time.sleep(10)
        auto.click(900,600)
        auto.click(900, 600)
    for i in range(20):
        auto.scroll(1000)
    kb.send('3')
    kb.send('3')

def otd():
   for i in range(30):
       auto.scroll(-1000)
def locx():
    try:
       auto.locateOnScreen('xxx.png',confidence=0.5)
    except:
        auto.locateOnScreen('four.png',confidence=0.5)
        nai()
    finally:
        return


#auto.doubleClick(x=342, y=785)
#time.sleep(8)
#auto.click(x=722, y=326)
#auto.click(x=634, y=812)
#auto.click(x=1007, y=804)
#loc0()
time.sleep(3)
print('первый')
while True:
   loc1()
   time.sleep(7)
   print('второй')
   loc2()
   time.sleep(7)
   bying()
   auto.click(x=1126, y=1057)
   loc3()
   time.sleep(7)
   otd()
   print('pohel')
   auto.click(x=625, y=545)
   auto.click(x=625, y=545)
   time.sleep(7)
   loc1()
   loc2()
   sale()
   time.sleep(7)
   auto.click(x=1126, y=1057)
   auto.click(x=1126, y=1057)
   loc3()
   otd()




