#цвета r 37 g 175 b 216
import time
import pyautogui as auto
import keyboard as kb
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
                kb.send(kb.shift)
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
        x = auto.locateOnScreen('two.png', confidence=0.9)
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
       c = auto.locateOnScreen('five3.png', confidence=0.6)
       print(c)
       l = c[0]
       print(l)
       l = l +15
       print(l)
       k = c[1]+10
       print (k)
       i =(l,k,0,0)
       print(k)
       auto.click(i)
       time.sleep(10)
       auto.click(1000,600)
       auto.click(1000, 600)
       for i in range(20):
           auto.scroll(1000)
    kb.send('3')
    kb.send('3')
def otd():
   for i in range(30):
       auto.scroll(-1000)
def nai2():
    pix = (39,72,23)
    x = 30
    y = 30
    a = True
    while a == True:
        r = auto.pixelMatchesColor(x, y, (pix), tolerance=50)
        while r == None:
            x = x +20
            y = y+5
    print(r)
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
               kb.press('shift')
               auto.click(z,y)
               kb.release('shift')
               r = auto.pixelMatchesColor(x, y, (0, 255, 0), tolerance=50)
            else:
               x = x +1
               y = y +1
               if x>=520:
                   x = x -10
        except OSError:
            auto.scroll(-550)
            return


time.sleep(1)
while True:
     auto.click(x=1261, y=953)
