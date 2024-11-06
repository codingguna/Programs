import cv2
import numpy as np
img=cv2.imread('download.jpeg',0)
cv2.imshow('input image',img)
imf=np.float32(img)
dst=cv2.dct(imf,cv2.DCT_INVERSE)
img1=cv2.idct(dst)
img1=np.uint8(img)
cv2.imshow('dct of input image',dst)
cv2.imshow('reconstructed image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
