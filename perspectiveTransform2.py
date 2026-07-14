import cv2
import numpy as np

img = cv2.imread("images/lane4perspectiveTR.png") # 400 x 138 pixels
cv2.imshow('Original', img)
h,w,_= img.shape
print(img.shape)

# Locate points of the object which you want to transform
pts1 = np.float32([[140,0], [310,0], [0, 138], [400, 138]])
# destination points                
pts2 = np.float32([[0, 0], [400, 0], [0, 138], [400, 138]])

# Apply Perspective Transform Algorithm
matrix = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(img, matrix, (400,138)) # 3rd param: size of output image
	
# Wrap the transformed image
cv2.imshow('Warped image', result) # Transformed Capture

if cv2.waitKey(0):
    cv2.destroyAllWindows()