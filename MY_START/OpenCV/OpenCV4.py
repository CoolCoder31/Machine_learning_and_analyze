import cv2
import numpy as np
img = cv2.imread("input.jpg")
# print(img.shape)
num_rows , num_cols = img.shape[:2]
translation_matrix = np.float32([[1,0,70],[0,1,110]])
img_translation = cv2.warpAffine(img,translation_matrix,(num_cols + 70 + 30,num_rows +110 + 30),cv2.INTER_,cv2.BORDER_WRAP,1)
cv2.imshow("IMAGE" , img_translation)
cv2.waitKey(0)
