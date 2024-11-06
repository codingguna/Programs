import cv2 
import numpy as np 
img=cv2.imread('download.jpeg',0) 
#row,col=img.shape
img1=np.zeros((img.shape[0],img.shape[1]),dtype = 'uint8')  

for i in range(img.shape[0]): 
    for j in range(img.shape[1]): 
        if img[i,j]>30 and img[i,j]<90: 
            img1[i,j] = 170 
        else: 
            img1[i,j] = 50 
cv2.imshow('Input image', img) 
cv2.imshow('Sliced image', img1) 
cv2.waitKey(0) 
cv2.destroyAllWindows()