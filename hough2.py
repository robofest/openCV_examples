#!/usr/bin/env python3

# Import OpenCV and NumPy
import cv2 as cv
import numpy as np

img = cv.imread("images/road3.jpg")
(rows,cols,channels) = img.shape
rows = int(rows*1/2)
cols = int(cols*1/2)
img = img[rows:rows+200, cols:cols+250] # keep lower right part

# Apply Canny edge detector using 
# https://pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/
v = np.median(img)
sigma = 0.23
l = int(max(0, (1.0 - sigma) * v))
u = int(min(255, (1.0 + sigma) * v))
#img_canny = cv.Canny(img, l, u)
img_canny = cv.Canny(img, 127, 255) # 

# Apply the Hough Transform to find lines
# HoughLinesP, where P means Probailistic
rho = 1 # distance precision in pixel, i.e. 1 pixel
angle = np.pi / 180  # angular precision in radian, i.e. 1 degree
min_threshold = 10  # minimal of votes
line_segments = cv.HoughLinesP(img_canny, rho, angle,
                               min_threshold, np.array([]),
                               minLineLength=10, maxLineGap=10)
print(line_segments.shape)
print(line_segments)
# Draw new image with lines
img_lines = img.copy()
if( line_segments is not None ):
    for line in line_segments:
        pts = line[0]
        pt1 = (pts[0],pts[1])
        pt2 = (pts[2],pts[3])
        color = 255
        thickness = 2
        cv.line(img_lines, pt1, pt2, color, thickness)
        print(f'Line ({pts[0]}, {pts[1]}) -> ({pts[2]}, {pts[3]})' )
    print(f"Tot # of line segments = {line_segments.shape[0]}")        
# Show the Canny image
cv.imshow('Source', img)
cv.imshow('Source + Canny Edges', img_canny)
cv.imshow('Source + Hough Lines', img_lines)
cv.waitKey(0)


