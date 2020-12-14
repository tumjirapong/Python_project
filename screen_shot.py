import numpy as np
import cv2
from PIL import ImageGrab
import win32api
import time
import pyautogui
import screeninfo

state_left  = win32api.GetKeyState(0x01) #Left button down = 0 or 1 . Button up = -127 or -128
state_right = win32api.GetKeyState(0x02) #Right button down = 0 or 1 . Button up = -127 or -128

screen_id = 0
screen = screeninfo.get_monitors()[screen_id]
screen_width, screen_height = screen.width, screen.height

while True:
    
    default_im = pyautogui.screenshot()
    default_im = cv2.cvtColor(np.array(default_im), cv2.COLOR_RGB2BGR)
    window_name = 'projector'
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow(window_name, default_im)
    cv2.waitKey(0)
    
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)
    
    if a != state_left:
        state_left = a 
        print(a)
        if a < 0:
            start_pos_x = pyautogui.position()[0]
            start_pos_y = pyautogui.position()[1]
            print('Left Button Pressed')
        else:
            end_pos_x = pyautogui.position()[0]
            end_pos_y = pyautogui.position()[1]
            print('Left Button Released')
            break
    time.sleep(0.001)
 
cv2.destroyAllWindows()  

    
width = end_pos_x - start_pos_x
height  = end_pos_y - start_pos_y
image = pyautogui.screenshot(region=(start_pos_x , start_pos_y , width , height))
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) 

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
    