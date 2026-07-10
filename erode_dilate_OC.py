import cv2 as cv
import numpy as np
 
img = cv.imread('images/j.png', cv.IMREAD_GRAYSCALE)
cv.imshow('original J', img)
assert img is not None, "file could not be read, check with os.path.exists()"
kernel = np.ones((5,5), np.uint8)

erosion = cv.erode(img, kernel, iterations = 1)
cv.imshow('Erosion', erosion)
dilation = cv.dilate(img,kernel,iterations = 1)
cv.imshow('Dilation', dilation)

opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
cv.imshow('Opening', opening)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
cv.imshow('Closing', closing)

cv.waitKey(0)
cv.destroyAllWindows()