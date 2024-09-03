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
    #BLANK IMAGE
    imgBlank=np.zeros((heightImg,widthImg,3),np.uint8)
    
    if webCamFeed:success, img=cap.read()
    else:img=cv2.imread(pathImage)
    img=cv2.resize(img,(widthImg,heightImg))