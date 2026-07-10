#!/usr/bin/env python3

#import numpy: the data structure that will handle an image
import numpy as np
import cv2

image_name = "blackwhite"
print ('read an image from file')
img = cv2.imread("images/"+image_name+".jpg")
print ('display the image')
cv2.imshow("bw", img)


print ('display the content of the image')
print (img)
print ('In Python, an image is stored in a numpy array.') 
print ('Numpy is library used for scientific computing of multi-dimensional arrays and matrices.')

print ('we can determine several features of the images using numpy array properties')
print (f'type of an image type(img): {type(img)}')
print (f'size of the image img.size: {img.size}')
print (f'length of the image (number of pixel in the vertical direction) len(img): {len(img)}')
print (f'shape of an image (length in pixe, width in pixel, number of color) img.shape {img.shape}')
print (f'image length (also height) img.shape[0]: {img.shape[0]}')
print (f'image width img.shape[1]: {img.shape[1]}')

height, width, channels = img.shape
print (f'height = {height}')
print (f'width = {width}')
print (f'channels = {channels}')

print (f'number of colors per pixel img.shape[2]: {img.shape[2]}')
print (f'number of pixels: {(img.shape[0]*img.shape[1])}')
print (f'type of the image img.dtype: {img.dtype}')
print (f'sub-image at row [10] (img[10])')
print (img[10])
print (f'shape of sub-image at row [0] (img[10].shape)')
print (img[10].shape)
print (f'pixel at raw 10 and column 5 (img[10, 5])')
print (img[10, 5])
print (img[10] [5])
print (f'pixel at raw 0 and column 0 (img[0, 0])')
print (img[0, 0])
print (img[0] [0])

print (f'you can see a single channel in the image, for example only the first channel')
print (img[:, :, 0])



cv2.waitKey(0) # needed to hold the displayed image in a Window frame
cv2.destroyAllWindows()