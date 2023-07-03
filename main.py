import pyautogui
import pygetwindow
import platform
from PIL import Image

path = '.\\result.png'
title = pygetwindow.getAllTitles()
sys = platform.system()

window = pygetwindow.getWindowsWithTitle('League of Legends')[0]
left, top = window.topleft
right, bottom = window.bottomright
pyautogui.screenshot(path)
im = Image.open(path)
im = im.crop((left, top, right, bottom))
im.save(path)
im.show(path)