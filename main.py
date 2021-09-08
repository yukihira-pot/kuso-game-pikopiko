from selenium import webdriver
import chromedriver_binary  
import pyautogui
import time

import RGB_for_each_y as c

def pix(x, y):
    '''座標(x, y)のRGBを取得'''
    try:
        p = pyautogui.pixel(x, y)
    except OSError:
        p = pyautogui.pixel(x, y)
    except:
        p = pyautogui.pixel(x, y)
    return p

def is_ok(pix, c, n):
    '''与えられたpixelが、cのインデックスn番目のpixelと等しいかどうかを出力'''
    return pix[0] == c[n][0] and pix[1] == c[n][1] and pix[2] == c[n][2]

# URL & File Name
URL = "https://jankara.ne.jp/kuso-game/pikopiko/attack"

# Open Web Browser & Resize
driver = webdriver.Chrome()
driver.set_window_size(1280, 900) 
driver.get(URL)

pyautogui.moveTo(1000, 800, 3)
pyautogui.mouseDown()
pyautogui.click(x = 1000, y = 300)
   

x = 510

flg = True
while flg:
    p1 = pix(750, 650)
    p2 = pix(900, 650)   
    if p1[0] == 0 and p1[1] == 0 and p1[2] == 0 \
    and p2[0] == 0 and p2[1] == 0 and p2[2] == 0:
        time.sleep(2)
        flg = False
        driver.quit()

    else:
        for j in range(5, 52, 6): 
            x_sub = x + 10 * j
            if is_ok(pix(x_sub, 600), c.c600, j) \
            and is_ok(pix(x_sub-20, 600), c.c600, j-2)\
            and is_ok(pix(x_sub+20, 600), c.c600, j+2)\
            and is_ok(pix(x_sub-60, 600), c.c600, j-6)\
            and is_ok(pix(x_sub+60, 600), c.c600, j+6):

                if is_ok(pix(x_sub, 700), c.c700, j) \
                and is_ok(pix(x_sub-20, 700), c.c700, j-2)\
                and is_ok(pix(x_sub+20, 700), c.c700, j+2)\
                and is_ok(pix(x_sub-60, 700), c.c700, j-6)\
                and is_ok(pix(x_sub+60, 700), c.c700, j+6):
                        '''
                    if is_ok(pix(x_sub, 400), c.c400, j) \
                    and is_ok(pix(x_sub-20, 400), c.c400, j-2)\
                    and is_ok(pix(x_sub+20, 400), c.c400, j+2)\
                    and is_ok(pix(x_sub-60, 400), c.c400, j-6)\
                    and is_ok(pix(x_sub+60, 400), c.c400, j+6):
                    '''
                        pyautogui.mouseDown()
                        pyautogui.click(x_sub, 900)

