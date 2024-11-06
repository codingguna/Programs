import cv2
import numpy as np
img=cv2.imread('download.jpeg',0)
img_new=np.zeros([img.shape[0],img.shape[1]])
for i in range(1,img.shape[0]-1):
    for j in range(1,img.shape[1]-1):
        temp=[img[i-1,j-1],img[i-1,j],img[i-1,j+1],img[i,j-1],img[i,j],img[i,j+1],img[i+1,j-1],img[i+1,j],img[i+1,j+1]]
        temp1=sorted(temp)
        img_new[i,j]=temp[4]
# img_new1=img_new.astype(np.uint8)
cv2.imshow('input',img)
cv2.imwrite('medianfilter.png',img_new)
cv2.imshow('median filter',cv2.imread('medianfilter.png'))
cv2.waitKey(0)
cv2.destroyAllWindows()
