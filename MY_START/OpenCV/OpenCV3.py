import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("input.jpg",cv2.IMREAD_COLOR)
pix = img[55:55]
img[55,55] = [255,255,255]#Changing of pixel
px = img[55,55]
# print(px)
#we can reference an ROI, or Region of Image
px = img[100:150,100:150]
# print(px)
img[100:150,100:150] = [255,255,255]
# print(px)
# print(img.shape)
# print(img.size)
# print(img.dtype)
watch_face = img[37:111,107:194]
img[0:74,0:87] = watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()