from io import BytesIO
import win32clipboard
from PIL import Image
import pyautogui as pag
import keyboard
import time

filepath = 'C:/workspace/python-ScreenCapture/image.jpg'

while True:
    if keyboard.is_pressed("f"):
        start = pag.position()
        print(start)
        time.sleep(0.2)
        break
while True:
    if keyboard.is_pressed("f"):
        end = pag.position()
        print(end)
        time.sleep(0.2)
        break

xx = start[0]
yy = start[1]
ww = end[0] - start[0]
hh = end[1] - start[1]


pag.screenshot(filepath, region = (xx,yy,ww,hh))

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

image = Image.open(filepath)

output = BytesIO()
image.convert("RGB").save(output, "BMP")
data = output.getvalue()[14:]
output.close()

send_to_clipboard(win32clipboard.CF_DIB, data)

