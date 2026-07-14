#!/usr/bin/env python3

import cv2 as cv
import numpy as np

image = cv.imread("images/road3crop.png")
h, w, _ = image.shape # note: height first
cv.imshow('Source', image)

# creating a mask of that has the same dimensions of the image
# mymask = np.zeros(image.shape[:2], dtype="uint8")
mymask = np.zeros((h, w), dtype="uint8")
# creating a rectangle on the mask
# where the pixels are valued at 255
#cv.rectangle(mymask, (0, 90), (290, 450), 255, -1) 

# polygon mask
#myROI = [(25, 0), (0, int(h/3)), (0, h), (w, h), (w, int(h/2)), (w-80, 0)]  # (x, y)
myROI = [(25, 0), (0, int(h/3)), (0, int(h/2)), (w, int(h/2)), (w-80, 0)]  # (x, y)
cv.fillPoly(mymask, [np.array(myROI)], 255) # 255-white color

cv.imshow("Mask", mymask)
print(f"image shape: {image.shape}")
print(f"mask shape: {mymask.shape}")
# performing a bitwise_and with the image and the mask
masked  = cv.bitwise_and(image, image, mask=mymask) # use this way when shapes are different
# masked = cv.bitwise_and(image, mask) -- Does not work. shapes are different
cv.imshow("Mask applied to Source Image", masked)

cv.waitKey(0)