#!/usr/bin/env python3

# https://medium.com/featurepreneur/draw-contours-on-an-image-using-opencv-186b67f87c92

import cv2 as cv

# Read the image
#img = cv.imread("images/shapes3.jpg")
#img = cv.imread("images/y-line-s.jpg")
img = cv.imread("images/StarTri.jpg")
cv.imshow('Original', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #convert to grayscale

# Blur image to *increase* contour dots
gray = cv.blur(gray, (3,3))

# Apply thresholding to the image
ret, thresh = cv.threshold(gray, 220, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# Find the contours in the "thresh" image
#contours, heirarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours, heirarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# Find centroid for each blob and print
# https://learnopencv.com/find-center-of-blob-centroid-using-opencv-cpp-python/
for c in contours:
    print(cv.contourArea(c))
    M = cv.moments(c)
    if M['m00'] != 0:
        cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
        print(f"x = {cx}     y = {cy}")
        
# https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
#cv.drawContours(img, contours, 2, (255,0,0), 3) # Draw one countour: 2 means the 3rd countour

# Draw all the obtained contour lines(or the set of coordinates forming a line) on the original image
cv.drawContours(img, contours, -1, (255,0,0), 3) # -1 means to draw all the countours

#show the image
cv.imshow('Contours', img)
if cv.waitKey(0):
    cv.destroyAllWindows()
