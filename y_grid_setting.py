import os
from selenium import webdriver
import chromedriver_binary  
from PIL import ImageGrab
import pyautogui
import time
import copy

# URL & File Name
URL = "https://jankara.ne.jp/kuso-game/pikopiko/attack"

# Open Web Browser & Resize
driver = webdriver.Chrome()
driver.set_window_size(1280, 900) 
driver.get(URL)

pyautogui.moveTo(1000, 300, 3)
pyautogui.mouseDown()
pyautogui.click(x = 1000, y = 300, clicks = 2)



FILENAME_pre = "C:\\Users\\rmago\\OneDrive\\Pictures\\Screenshots"
# Get Screen Shot
'''
for i in range(10):
    screenshot = pyautogui.screenshot(region = (501, 165, 623, 860))
    screenshot.save(FILENAME_pre + "\\" + "screenshot" + str(i) +  ".png")
'''


x = 400
y = 700

c = []
# x = 510からx = 1110まで、10間隔のの60段階で、定められたy座標におけるRGB値を取得します
for i in range(60):
    try:
        pix = pyautogui.pixel(x, y)
    except OSError:
        pix = pyautogui.pixel(x, y)
    except:
        pix = pyautogui.pixel(x, y)
    c.append(list(pix))
    x += 10

print("")
print(c)



driver.quit()