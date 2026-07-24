#!/usr/bin/env python3

import cv2 as cv
import numpy as np

road = cv.imread("images/road.PNG")
(rows, cols, channel) = road.shape
cv.imshow("Road",road)

barrel = cv.imread("images/barrel.PNG")
# Resize barrel to match road dimensions
barrel = cv.resize(barrel, (cols, rows)) # to make sure the same size
cv.imshow("Barrel",barrel)

bitwiseAnd = cv.bitwise_and(road, barrel)
cv.imshow("AND",bitwiseAnd)

bitwiseOR = cv.bitwise_or(road, barrel)
cv.imshow("OR", bitwiseOR)

# Subtract AND image from road
subtracted = cv.subtract(road, bitwiseAnd)
cv.imshow("Road minus AND", subtracted)

cv.waitKey(0)