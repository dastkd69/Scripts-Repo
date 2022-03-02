import time
import cv2
import numpy as np
import keyboard
from PIL import ImageGrab
from win32api import GetSystemMetrics

# display screen resolution, get it from your OS settings
Width = GetSystemMetrics(0)
Height = GetSystemMetrics(1)
SCREEN_SIZE = (Width, Height)
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# create the video write object
out = cv2.VideoWriter("output.avi", fourcc, 24.0, (SCREEN_SIZE))

last = time.time()
while True:
    # make a screenshot
    frame = np.array(ImageGrab.grab() )
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)
    # show the 
    print("The screen printed at {}".format(time.time()-last))
    #cv2.imshow("screenshot", frame)
    # if the user clicks q, it exits
    last = time.time()
    if keyboard.is_pressed("q"):
        print("You pressed q")
        break
out.release()    