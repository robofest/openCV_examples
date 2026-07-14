#!/usr/bin/env python3

# Import OpenCV and NumPy
import cv2 as cv
import numpy as np

# Define a blank, grayscale image
img = np.zeros( shape=(300, 300,1), dtype='uint8')

# Draw a rectangle
pt1 = (100,100)
pt2 = (200,220)
color = (75, 75, 75) # gray
thickness = -1 # fill in
cv.rectangle(img, pt1, pt2, color, thickness)

# Apply Canny edge detector
img_canny = cv.Canny(img, 0, 32) # thresh1, thresh2

# Apply the Hough Transform to find lines
# HoughLinesP, where P means Probailistic
rho = 1   # distance precision in pixel, i.e. 1 pixel
angle = np.pi / 180  # angular precision in radian, i.e. 1 degree
min_threshold = 10   # minimal of votes
line_segments = cv.HoughLinesP(img_canny, rho, angle,
                               min_threshold, np.array([]),
                               minLineLength=10, maxLineGap=10)
# Draw new image with lines
img_lines = img.copy()
if( line_segments is not None ):
    for line in line_segments:
        pts = line[0]
        pt1 = (pts[0],pts[1])
        pt2 = (pts[2],pts[3])
        color = 255
        thickness = 1
        cv.line(img_lines, pt1, pt2, color, thickness)
        print('Line (%d,%d) -> (%d,%d)' % (pts[0], pts[1], pts[2], pts[3]))
        #print(f'Line ({pts[0]}, {pts[1]}) -> ({pts[2]}, {pts[3]})' )
cv.imshow('Source', img)
cv.imshow('Source + Hough Lines', img_lines)
cv.imshow('Source + Canny Edges', img_canny)
cv.waitKey(0)
