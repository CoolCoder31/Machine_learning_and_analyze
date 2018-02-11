#how to import video in openCV
import cv2 as cv2
import matplotlib.pyplot as plt
import numpy as np
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('outpu.avi',fourcc,20.0,(640,480))
while(cap.isOpened()):
    ret, frame = cap.read()#This code initiates an infinite loop
    #ret for boolean reagrading it returns or not
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#OpenCV reads colors as BGR (Blue Green Red),
    # where most computer applications read as RGB
    # (Red Green Blue)
    cv2.imshow('FRAME',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cap.destroyAllWindows()