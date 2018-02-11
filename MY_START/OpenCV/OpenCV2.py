import cv2 as cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread("input.jpg",cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150),(225,225,225),15)
cv2.rectangle(img,(15,25),(200,150),(0,0,255),15)
cv2.circle(img,(50,50),25,(225,225,225),20)
cv2.imshow("IMAGE",img)
cv2.waitKey(0)
cv2.destroyAllWindows()