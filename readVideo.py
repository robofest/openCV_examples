#!/usr/bin/env python3
import cv2

# read video from webcam

capture = cv2.VideoCapture(0) # 0: webcam id
while True:
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1) # flip to see ourselves in a mirror
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    # fx and fy to scale
    cv2.imshow("webcam", frame)
    # waitKey(30): the captured image will remain 30 milliseconds on the screen
    # returns -1, if no key entered. ASCII value, when a key is entered
    if cv2.waitKey(30) != -1: 
        break

capture.release()
cv2.destroyAllWindow()