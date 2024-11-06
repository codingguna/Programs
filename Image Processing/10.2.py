import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('guna.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,threshold=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel=np.ones((3,3),np.uint8)
opening=cv2.morphologyEx(threshold,cv2.MORPH_OPEN,kernel,iterations=2)
sur_bg=cv2.dilate(opening,kernel,iterations=3)
dist_tran=cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret,sur_fg=cv2.threshold(dist_tran,0.7*dist_tran.max(),255,0)
sur_fg=np.uint8(sur_fg)
unknown=cv2.subtract(sur_bg,sur_fg)
ret,markers=cv2.connectedComponents(sur_fg)
markers+=1
markers[unknown==255]=0
cv2.watershed(img,markers)
colored_marker=np.zeros_like(img)
colored_marker[markers==-1]=[0,255,0]
segment_img=cv2.addWeighted(img,0.7,colored_marker,0.7,0)
cv2.imshow('input',img)
cv2.imshow('segmented img',segment_img)
cv2.waitKey(0)
cv2.destroyAllWindows()