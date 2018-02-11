import cv2 as cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread("input.jpg",cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150),(225,225,225),15)
cv2.rectangle(img,(215,225),(300,350),(0,0,255),15)
cv2.circle(img,(250,250),25,(225,225,225),20)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# OpenCV documentation had this code, which reshapes the array to a 1 x 2. I did not
# find this necessary, but you may:
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,"OpenCV",(350,430),font,2,(0,0,0),13)

cv2.imshow("IMAGE",img)
cv2.waitKey(0)
cv2.destroyAllWindows()