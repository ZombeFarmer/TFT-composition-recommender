import time
import numpy as np
import cv2
import pyautogui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys
import pygetwindow
import platform
from PIL import Image

# path = '.\\result.png'
# title = pygetwindow.getAllTitles()
# sys = platform.system()
SCREEN_SIZE = (2560 , 1440)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi",fourcc,20.0,(SCREEN_SIZE))
fps = 1
prev = 0
while True:
    time_elapsed = time.time() - prev
    img = pyautogui.screenshot()
    #if (time_elapsed > 1.0/fps):
    #prev = time.time()
    frame = np.array(img)
    print(frame)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    #cv2.waitKey(100)
cv2.destroyAllWindows()
out.release()
# window = pygetwindow.getWindowsWithTitle('League of Legends')[0]
# left, top = window.topleft
# right, bottom = window.bottomright
# pyautogui.screenshot(path)
# im = Image.open(path)
# im = im.crop((left, top, right, bottom))
# im.save(path)
# im.show(path)