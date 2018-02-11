#how to import video in openCV
import cv2 as cv2
import matplotlib.pyplot as plt
import numpy as np
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('FRAME',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cap.destroyAllWindows()