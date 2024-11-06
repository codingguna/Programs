import cv2 
import numpy as np 
img=cv2.imread('download.jpeg',0) 
row,col=img.shape
img1=np.zeros((row,col),dtype = 'uint8')  
min_range=30 
max_range=90  
for i in range(row): 
    for j in range(col): 
        if img[i,j]>min_range and img[i,j]<max_range: 
            img1[i,j] = 170 
        else: 
            img1[i,j] = img[i,j]
cv2.imshow('Input image', img) 
cv2.imshow('Sliced image', img1) 
cv2.waitKey(0) 
cv2.destroyAllWindows()