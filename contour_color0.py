#!/usr/bin/env python3

# Find target color blob, draw contour lines / centroid dot of largest

import cv2 as cv
import numpy as np

img = cv.imread("images/shapes2.jpg")
#img = cv.imread("images/StarTri.jpg")
cv.imshow('Original', img)
img = cv.medianBlur(img, 5)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# lower, upper, to get blue, 90 < H < 150
thresh = cv.inRange(hsv,np.array((100, 80, 80)), np.array((140, 255, 255))) 

# lower, upper, to get yellow, 22 < H < 45
#thresh = cv.inRange(hsv,np.array((22, 93, 0)), np.array((45, 255, 255))) 
cv.imshow('Thresh', thresh)

# find contours in the threshold image
contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, (0,0,255), 10) # -1: draw all contour lines

max_area = 0
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
#cv.drawContours(img, max_c, -1, (0,0,255), 10)

# finding centroids of max contour and draw a circle there
# https://www.geeksforgeeks.org/python-opencv-find-center-of-contour/
# https://learnopencv.com/find-center-of-blob-centroid-using-opencv-cpp-python/
M = cv.moments(max_c)
cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
# https://www.geeksforgeeks.org/python-opencv-cv2-circle-method/
cv.circle(img, (cx,cy), 10, (0,0,0), -1) # -1 fill the circle

#show the image
cv.imshow('Contours with centroid dot', img)

if cv.waitKey(0):
    cv.destroyAllWindows()
