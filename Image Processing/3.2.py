import cv2 
import matplotlib.pyplot as plt 
img = cv2.imread('download.jpeg', cv2.IMREAD_GRAYSCALE) 
cv2.imshow('Input Image',img) 
plt.hist(img.flatten(),256,[0,256], color = 'r') 
plt.show() 
equ = cv2.equalizeHist(img) 
cv2.imshow('Equalized',equ)
plt.hist(equ.flatten(),256,[0,256], color = 'r') 
plt.show() 
cv2.waitKey(0) 
cv2.destroyAllWindows()