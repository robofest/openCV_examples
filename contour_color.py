#!/usr/bin/env python3
import cv2 as cv
import numpy as np
#read the image
#img = cv.imread("images/shapes2.jpg")
img = cv.imread("images/StarTri.jpg")

img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)

#cv.imshow('Original', img)
# convert to hsv and find range of colors
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# lower, upper, to get blue, 90 < H < 150
thresh = cv.inRange(hsv,np.array((100, 80, 80)), np.array((140, 255, 255))) 

# lower, upper, to get yellow, 22 < H < 45
# thresh = cv.inRange(hsv,np.array((22, 93, 0)), np.array((45, 255, 255))) 
# thresh = cv.inRange(hsv,np.array((0, 20, 100)), np.array((50, 255, 255))) 
#thresh2 = thresh.copy()

# find contours in the threshold image
contours,hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
if contours is None:
    exit()
cv.drawContours(img, contours, -1, (0,0,255), 10)
cv.imshow('Yellow objects', img)
max_area = 0
max_c = None
for c in contours:
    print(cv.contourArea(c))
    M = cv.moments(c)
    if M['m00'] != 0:
        cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
        print(f"x = {cx}     y = {cy}")
        area = cv.contourArea(c)
        if area > max_area:
            max_area = area
            max_c = c

#draw the obtained contour lines(or the set of coordinates forming a line) on the original image
cv.drawContours(img, max_c, -1, (0,0,255), 10)

# finding centroids of max contour and draw a circle there
# https://www.geeksforgeeks.org/python-opencv-find-center-of-contour/
# https://learnopencv.com/find-center-of-blob-centroid-using-opencv-cpp-python/
M = cv.moments(max_c)
if M['m00'] != 0:
    cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    # https://www.geeksforgeeks.org/python-opencv-cv2-circle-method/
    cv.circle(img, (cx,cy), 10, (0,0,0), -1) # -1 fill the circle

#show the image
cv.imshow('Contours', img)
cv.imshow('Thresh', thresh)
if cv.waitKey(0):
    cv.destroyAllWindows()
