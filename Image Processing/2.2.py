import cv2
import numpy as np
img1 = cv2.imread('download.jpeg')
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img_flt=np.float32(img)
c=255/np.log(1+np.max(img_flt))
log_img=c*(np.log(1+img_flt))
log_img=np.uint8(log_img)
cv2.imshow('original',img1)
cv2.imshow('gray scale img',img)
cv2.imshow('log ing',log_img)
cv2.waitKey(0)
cv2.destroyAllWindows()