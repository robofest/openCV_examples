#!/usr/bin/env python3

import cv2 as cv
import numpy as np
# creating a square of zeros using a variable
rectangle = np.zeros((300, 300), dtype="uint8")
cv.rectangle(rectangle, (50, 50), (250, 250), 127, -1) # paint gray box on black
cv.imshow("Rectangle (source)", rectangle)

# creating a circle of zeros using a variable
circle = np.zeros((300, 300), dtype="uint8")
cv.circle(circle, (150, 150), 120, 255, -1)
cv.imshow("Circle (source)", circle)

bitwiseNot = cv.bitwise_not(circle)
cv.imshow("Not Circle", bitwiseNot)

bitwiseAnd = cv.bitwise_and(rectangle, circle)
masked = cv.bitwise_and(rectangle, rectangle, mask=circle) # same as And
cv.imshow("Rectangle AND Circle", bitwiseAnd)

bitwiseOR = cv.bitwise_or(rectangle, circle)
cv.imshow("Rectangle OR Circle", bitwiseOR)

cv.waitKey(0)