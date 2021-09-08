import os
from selenium import webdriver
import chromedriver_binary  
from PIL import ImageGrab
import pyautogui
import time

# URL & File Name
URL = "https://jankara.ne.jp/kuso-game/pikopiko/attack"

# Open Web Browser & Resize
driver = webdriver.Chrome()
driver.set_window_size(1280, 900) 
driver.get(URL)

pyautogui.moveTo(1000, 800, 1.5)
pyautogui.mouseDown()
pyautogui.click(x = 1000, y = 300, clicks = 2)

while True:
    x, y = pyautogui.position()
    # 現在位置の出力
    print(x, y)
    # 現在位置のRGBの出力
    try:
        p = pyautogui.pixel(x, y)
    except OSError:
        p = pyautogui.pixel(x, y)
    except:
        p = pyautogui.pixel(x, y)
    print(p)
    time.sleep(3)