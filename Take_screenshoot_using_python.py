#-----taking screenshoot--☺
import numpy
import cv2
import pyautogui
img=pyautogui.screenshot()
imgs=cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
cv2.imwrite('image.png', imgs)
