import cv2 as cv

image = cv.imread("images/road1.jpg")
h, w, _ = image.shape # note: height first
print(f"Original image size: {w}x{h}")
cv.imshow('Source', image)

# Resize the image to 640x480
new_size = (640, 480) # dsize is (width, height)
resized_image1 = cv.resize(image, new_size, interpolation=cv.INTER_AREA)
print(f"Resized image1 size: {new_size[0]}x{new_size[1]}")
cv.imshow('Resized1', resized_image1)

# resize the image to half its original size using scale factors; dsize is None
resized_image2 = cv.resize(image, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
print(f"Resized image2 size: {resized_image2.shape[1]}x{resized_image2.shape[0]}")
cv.imshow('Resized2', resized_image2)

cv.waitKey(0)
cv.destroyAllWindows() 