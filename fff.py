import pyautogui as auto
import time
#r = auto.screenshot(region=(500,300,30,400))
#r.save('1.png')
#a = auto.getpixel((502,200))
#print(a)
#a= auto.pixelMatchesColor(r,(17, 16, 11)tolerance=40)
#print(a)
#width=1920, height=1080

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
        
sale()


