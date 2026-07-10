#!/usr/bin/env python3
#
# ONLY ESC will terminate the program
# Linux Python allowed callback
# Windows Python callback function worked, but error messages
# This version is changed for Windows.
#
import cv2 as cv
import sys

# https://www.geeksforgeeks.org/python-opencv-canny-function/

# Parameters
thres1 = 0
thres2 = 0
aperture = 0
aperture_list = [3,5,7]

# Canny trackbar callback
# def callback(x):
#     global thres1, thres2, aperture
#     thres1 = cv.getTrackbarPos('thres1','controls')
#     thres2 = cv.getTrackbarPos('thres2','controls')
#     aperture = cv.getTrackbarPos('aperture_3_5_7','controls')
#     return
def nothing(x):
    pass

# Create the a controls window
cv.namedWindow('controls', 2) # to create a window for displaying images or GUI elements like trackbars. 
# This must be called before creating trackbars or displaying images

# Create trackbars for canny thresholds
cv.createTrackbar('thres1','controls',    0, 255, nothing) # 0 is imitial value
cv.createTrackbar('thres2','controls',    50, 255, nothing ) # 50 is initial value
cv.createTrackbar('aperture_3_5_7','controls',  0, 2, nothing)

# Read an image
#img = cv.imread(sys.argv[1])
img = cv.imread("images/road1.jpg")
#img = cv.imread("images/road2.png")

# img = cv.GaussianBlur(img, (5,5), 0)
# img = cv.blur(img, (5,5), 0)  # averaging
if img is None:
    print("Failed to load image. Check file path.")
    exit()
blur_kernel = 5
img = cv.medianBlur(img, blur_kernel)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Loop for edits
while(1):

    # Show the image
    cv.imshow('Source', img)
    thres1 = cv.getTrackbarPos('thres1','controls')
    thres2 = cv.getTrackbarPos('thres2','controls')
    aperture = cv.getTrackbarPos('aperture_3_5_7','controls')
    # Convert to grayscale. Canny is only for grayscale images
    # img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) -- No need to be inside loop!

    # Apply Canny edge detector
    img_canny = cv.Canny(img_gray, thres1, thres2,
                         apertureSize=aperture_list[aperture])

    # Show the Canny image
    cv.imshow('Canny', img_canny)

    # Exit on key enter
    k = cv.waitKey(1) & 0xFF
    if k == 27: # Esc
        break
                
# Close all windows
cv.destroyAllWindows()
