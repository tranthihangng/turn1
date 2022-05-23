# turn1

import cv2
import  imutils
import aiopytesseract


image = r"C:\Users\NEC 01\Downloads\Screenshot 2020-11-13 105906.jpg"
image = cv2.imread(image)
image = imutils.resize(image, width  = 500)
cv2.imshow('original image', image)
cv2.waitKey(0) #until press any key to go futher

# turn image to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray scale image", gray)
gray = cv2.bilateralFilter(gray, 11,17,17)
cv2. imshow('smoother image', gray)
cv2.waitKey(0)

#find the edged
edged = cv2.Canny(gray, 170,200)
cv2.imshow('canny edge', edged)
cv2.waitKey(0)

# find the contours
cnts, new = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image1 = image.copy()
cv2. drawContours(image1, cnts, -1,(0,255,0), 3)
cv2.imshow("canny after contouring", image1)
cv2.waitKey(0)

cnts = sorted(cnts, key= cv2.contourArea, reverse= True)[:30]
numberplatecount = None
image2 = image.copy()
cv2.drawContours(image2, cnts, -1, (0,255,0), 3)
cv2.imshow('top 30 contours', image2)
cv2.waitKey(0)

count = 0
name = 1
for i in cnts:
    perimeter = cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, 0.02*perimeter,True)

    if len(approx) ==4:
        numberplatecount = approx
        x,y ,w, h = cv2.boundingRect(i)
        crp_img = image[y:y+h, x: x+w]
        cv2.imwrite(str(name)+ '.png', crp_img)
        name+=1
        break
cv2.drawContours(image,[numberplatecount], -1, (0,255,0),3)
cv2.imshow('final image', image)
cv2.waitKey(0)
