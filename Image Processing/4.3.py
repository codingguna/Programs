import cv2
import numpy as np
img=cv2.imread('noise.jpeg')
sharp_filter=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
shapr_img=cv2.filter2D(img,-1,sharp_filter)
cv2.imshow('input',img)
cv2.imshow('sharpen',shapr_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 