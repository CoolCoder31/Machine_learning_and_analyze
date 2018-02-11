import cv2 as cv2
import numpy as np
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open WEB CAM")
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,None,fx=1,fy=1,interpolation=cv2.INTER_AREA)
    cv2.imshow('input',frame)

    c = cv2.waitKey(1)
    if c == 27:
        break
cap.release()
cap.destroyAllWindows()