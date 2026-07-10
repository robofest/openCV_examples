#!/usr/bin/env python3 
import cv2  
print(cv2.__version__)
import numpy as np 

def init_blob_detector():
    params = cv2.SimpleBlobDetector_Params()
    params.minThreshold = 1
    params.maxThreshold = 255
    params.filterByArea = False
    params.minArea = 1   # min pixels
    params.filterByCircularity = True
    params.filterByConvexity = False
    params.filterByInertia = False    # how elongated (stretched) a shape is
    #detector = cv2.SimpleBlobDetector(params) # OLD. itwill cause seg fault
    detector = cv2.SimpleBlobDetector_create(params)
    return detector 
   
img = cv2.imread("images/shapes.png", cv2.IMREAD_GRAYSCALE)

# To set up the detector with default parameters  
#   detector = cv2.SimpleBlobDetector_create()

detector = init_blob_detector()

# Detecting blobs's keypoints
keypoints = detector.detect(img)  # <===  must use SimpleBlobDetector_create

# Draw detected blobs as red circles.  
#   cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle 
#   corresponds to the size of blob  
img_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255),  
                                       cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)  
# Show keypoints  
cv2.imshow("Keypoints", img_with_keypoints)  
cv2.waitKey(0)

# more info: https://learnopencv.com/blob-detection-using-opencv-python-c/
