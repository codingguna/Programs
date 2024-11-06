import cv2 
import numpy as np 
img = cv2.imread('guna.jpg',0) 
minv=np.min(img)
maxv=np.max(img)
minmax_img = np.zeros((img.shape[0],img.shape[1]),dtype = 'uint8')
for i in range(img.shape[0]):
    for j in range(img.shape[1]): 
        minmax_img[i,j] = 255*(img[i,j]-minv)/(maxv-minv) 
cv2.imshow('Original Image',img) 
cv2.imshow('Contrast Stretched',minmax_img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
