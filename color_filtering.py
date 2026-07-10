#!/usr/bin/env python3 

import numpy as np
import cv2

image = cv2.imread("images/tennisball05.jpg")
cv2.imshow("Original",image)

#convert the BGR image into the HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv image",hsv)

#find the upper and lower bounds of the yellow color (tennis ball)
yellowLower =(22, 120, 100) # H, S, V
yellowUpper = (45, 255, 255) # H, S, V

#define a mask using the lower and upper bounds of the yellow color 
mask = cv2.inRange(hsv, yellowLower, yellowUpper)

cv2.imshow("mask image", mask)

cv2.waitKey(0) # click on a Window and enter any key
cv2.destroyAllWindows()