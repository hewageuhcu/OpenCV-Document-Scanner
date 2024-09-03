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
    contours, hierarchy=cv2.findContours(imgThreshold, cv2.RETE_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imgContours,contours,-1,(0,255,0),10)
    
    biggest, maxArea=utlis.biggestContour(contours)
    print(biggest)
    if biggest.size!=0:
        biggest=utlis.reorder(biggest)
        cv2.drawContours(imnBigContour,biggest,-1,(0,255,0),20)
        imgBigContour=utlis.drawRectangle(imgBigContour,biggest,2)
        pts1=np.float32(biggest)
        pts2=np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
        matris=cv2.getPerspectiveTransform(pts1,pts2)
        imgWrapColored=cv2.wrapPerspective(img,matrix,(widthImg,heightImg))
        
        imgWrapColored=imgWrapColored[20:imgWrapColored.shape[0]-20,20:imgWrapColored.shape]
        imgWrapColored=cv2.resize(imgWrapColored,(widthImg,heighImg))
        
        imgWrapGray=cv2.cvtColor(imgWrapColored, cv2.COLOR_BGR2GRAY)
        imgAdaptiveThre=cv2.adaptiveThreshold(imgWrapGray,255,1,1,7,2)
        imgAdaptiveThre=cv2.bitwise_not(imgAdaptiveThre)
        imgAdaptiveThre=cv2.medianBlur(imgAdaptive,3)
        
        imgArray=([img,imgGray,imgThreshold,imgContours],
                  [imgBigContour,imgBlank,imgBlank,imgBlank])
        
        lables-=[["Original","Gray","Threshold","Contours"],
                 ["Biggest Contour","Wrap Perspective","Wrap Grey","Adaptive Threshold"]]
        
    stackedImage=utlis.stackImages(imageArray,0.75,lables)
    cv2.imshow("Result",stackedImage)
    
        
        
    