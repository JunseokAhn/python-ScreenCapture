from io import BytesIO
import win32clipboard
import win32gui
from win32gui import FindWindow, GetWindowRect
from PIL import Image
import pyautogui as pag
import keyboard
import time
import math

filepath = 'C:/workspace/python-ScreenCapture/image.jpg'

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()
    
while True:
    if keyboard.is_pressed("f"):

        window_name = win32gui.GetWindowText (win32gui.GetForegroundWindow())
        window_handle = FindWindow(None, window_name)
        window_rect   = GetWindowRect(window_handle)

        print(window_name)
        print(window_rect)

        xx, yy, ww, hh = window_rect
        ww = ww-xx
        hh = hh-yy

        pag.screenshot(filepath, region = (xx,yy,ww,hh))

        image = Image.open(filepath)

        # width = 661.4173228346
        # height = 850.3937007874

        cm_width = 17.5
        cm_height = 22.5

        width_to_px = 37.79527559054857
        height_to_px = 37.79527559055111

        px_width = math.floor(cm_width * width_to_px)
        px_height = math.floor(cm_height * height_to_px)

        new_image = image.resize((px_width, px_height))
        new_image.save(filepath)



        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()

        send_to_clipboard(win32clipboard.CF_DIB, data)
    
    if keyboard.is_pressed("g"):
        print("exit")
        break

# if you want to select position
# while True:
#     if keyboard.is_pressed("f"):
#         start = pag.position()
#         print(start)
#         time.sleep(0.2)
#         break
# while True:
#     if keyboard.is_pressed("f"):
#         end = pag.position()
#         print(end)
#         time.sleep(0.2)
#         break

# xx = start[0]
# yy = start[1]
# ww = end[0] - start[0]
# hh = end[1] - start[1]
