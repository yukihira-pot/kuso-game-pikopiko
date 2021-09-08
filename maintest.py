'''mainではRGB値の全てを比較していましたが、
こちらではR値のみを比較してなけなしの高速化を図っています'''

from selenium import webdriver
import chromedriver_binary  
import pyautogui
import time

import RGB_for_each_y_test as c

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
    '''与えられたpixelが、cのインデックスn番目のpixelのR値と等しいかどうかを出力'''
    return pix[0] == c[n]

# URL
URL = "https://jankara.ne.jp/kuso-game/pikopiko/attack"

# ブラウザを開いて画面サイズを変更
driver = webdriver.Chrome()
driver.set_window_size(1280, 900) 
driver.get(URL)

# ゲーム開始
pyautogui.moveTo(1000, 800, 3)
pyautogui.mouseDown()
pyautogui.click(x = 1000, y = 300) 

# 移動可能な座標を全探索
x = 510
flg = True
while flg:

    p1 = pix(750, 650)
    p2 = pix(900, 650)  
    # ゲーム終了時にブラウザを閉じてプログラムを終了 
    if p1[0] == 0 \
    and p2[0] == 0:
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
                        pyautogui.mouseDown()
                        pyautogui.click(x_sub, 900)
