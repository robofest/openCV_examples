import cv2
import numpy as np

img = cv2.imread('images/road1.jpg')
rows, cols, _ = img.shape
r = int(rows*1/2)
c = int(cols*1/2)
img = img[r:r+220, c:c+360] # lower right part

cv2.imwrite('images/road1crop2.png',img)
cv2.imshow("Cropped", img)
print(img.shape)
cv2.waitKey(0)