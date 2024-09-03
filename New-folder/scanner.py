import cv2
import numpy as np
import utils  # Corrected from 'utlis' to 'utils'



##################################################
webCamFeed = True
pathImage = "OIP.jpg"
cap = cv2.VideoCapture(1)
cap.set(10, 160)
heightImg = 640
widthImg = 480
##################################################



utils.initializeTrackBars()  

while True:
    # BLANK IMAGE
    imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)

    if webCamFeed:
        success, img = cap.read()
    else:
        img = cv2.imread(pathImage)
    
    img = cv2.resize(img, (widthImg, heightImg))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    thres = utils.valTrackbars()  # Corrected from 'utlis' to 'utils'
    imgThreshold = cv2.Canny(imgBlur, thres[0], thres[1])
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgThreshold, kernel, iterations=2)
    imgThreshold = cv2.erode(imgDial, kernel, iterations=1)

    # find all contours
    imgContours = img.copy()
    imgBigContour = img.copy()  # Assuming you intended to use this variable; corrected typo
    contours, hierarchy=cv2.findContours(imgThreshold, cv2.RETE_EXTERNAL, cv2.CHAIN_APPROX_)