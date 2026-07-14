import cv2
import numpy as np

img = cv2.imread("images/road1crop2.png") # 220 x 360 (h x w)
h,w,_= img.shape
print(img.shape)
cv2.imshow('Original', img)

p1 = np.float32([[95, 0], [180, 0],  [0, 220], [360, 220]])            
p2 = np.float32([[0,  0], [360, 0],  [0, 220], [360, 220]])

# Apply Perspective Transform Algorithm
matrix = cv2.getPerspectiveTransform(p1, p2)
result = cv2.warpPerspective(img, matrix, (360,220)) # 3rd param: size of output image
	
# Wrap the transformed image 
cv2.imshow('Warped image', result) # Transformed Capture

if cv2.waitKey(0):
    cv2.destroyAllWindows()