import cv2
import numpy as np
img=cv2.imread('noise.jpeg')
k=int(input('enter size of kernel: '))
img_rst=cv2.medianBlur(img,k)
cv2.imshow('input',img)
cv2.imwrite('clearimg.png',img_rst)
cv2.imshow('clear img',cv2.imread('clearimg.png'))
cv2.waitKey(0)
cv2.destroyAllWindows()
