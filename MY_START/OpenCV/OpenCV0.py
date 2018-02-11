#how to read images and write images plot on matplotlib
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("input.jpg",cv2.IMREAD_GRAYSCALE)
# cv2.imshow("IMAGE",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#using matplotlib
plt.imshow(img,cmap='gray',interpolation = 'bicubic')
plt.xticks([])#to hide the scale on x axis
plt.yticks([])#to hide the scale on y axis
plt.plot([200,300,400],[100,200,300],'c',linewidth = 5)#to see line of width 5 and the coordinates
plt.show() # to display images
#to save the image
cv2.imwrite("IMAGE.png",img,None)