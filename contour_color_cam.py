#!/usr/bin/env python3

#
# Find the largest target color blob
# adapted from https://code-examples.net/en/q/c58032
#

import cv2
import numpy as np

# create video capture
cam = cv2.VideoCapture(0)

while(1):

    # read the frames
    _,frame = cam.read()

    # Smooth it
    #frame = cv2.blur(frame,(9,9))
    frame = cv2.medianBlur(frame, 5)
    
    # convert to hsv and find range of colors
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv,np.array((90, 80, 80)), np.array((150, 255, 255))) # lower, upper, to get blue, 90 < H < 150

    # find contours in the threshold image
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    # finding contour with maximum area and store it as best_cnt
    max_area = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max_area:
            max_area = area
            best_cnt = cnt

    # finding centroids of best_cnt and draw a circle there
    # https://www.geeksforgeeks.org/python-opencv-find-center-of-contour/
    M = cv2.moments(best_cnt)
    cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    cv2.circle(frame,(cx,cy), 15, (0,0,255), -1) # -1: fill the circle

    # Show it, if key pressed is 'Esc', exit the loop
    fr = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('With a centroid dot', fr)
    thr = cv2.resize(thresh, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Thresh', thr)
    if cv2.waitKey(33)== 27: # Esc key
        break

# Clean up everything before leaving
cv2.destroyAllWindows()
cap.release()
