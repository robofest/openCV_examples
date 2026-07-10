#!/usr/bin/env python3
import cv2
import numpy as np

img = cv2.imread("images/brain.jpg")
cv2.imshow("original w noise", img)

ksize = (5, 5)
stdb = cv2.blur(img, ksize)
cv2.imshow('std blur', stdb)

# https://en.wikipedia.org/wiki/Median_filter
# median blur smooths and preserve edges
blur_kernel = 5 # must be odd, 1, 3, 5, 7 ...
median = cv2.medianBlur(img, blur_kernel)
cv2.imshow('median filtered', median)

cv2.waitKey(0)
cv2.destroyAllWindows