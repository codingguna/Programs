import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread ("guna.jpg",0)
img_gaussian=cv2.GaussianBlur(img,(3,3),0)

img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=3)
img_sobely=cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=3)
img_sobel=img_sobelx+img_sobely

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx=cv2.filter2D(img_gaussian,-1,kernelx)
img_prewitty=cv2.filter2D(img_gaussian,-1,kernely)
img_prewitt=img_prewittx+img_prewitty

plt.subplot(3,3,2)
plt.imshow(img,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title("original image")

plt.subplot(3,3,4)
plt.imshow(img_sobelx,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('sobel x')

plt.subplot(3,3,5)
plt.imshow(img_sobely,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title("sobel y")

plt.subplot(3,3,6)
plt.imshow(img_sobel,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('sobel edges')

plt.subplot(3,3,7)
plt.imshow(img_prewittx,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('prewitt x')

plt.subplot(3,3,8)
plt.imshow(img_prewitty,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('prewitt y')

plt.subplot(3,3,9)
plt.imshow(img_prewitt,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('prewitt edges')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()