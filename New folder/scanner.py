import cv2
import numpy as np
import utlis

##################################################
webCamFeed=True
pathImage="OIP.jpg"
cap=cv2.VideoCapture(1)
cap.set(10,160)
heightImg=640
widthImg=480
##################################################

utlis.intializeTrackBars()
count=0

while true: