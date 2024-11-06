import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('coin.jpg')
plt.subplot(1,2,1)
plt.imshow(img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
pixel_val=img.reshape((-1,3))
pixel_val=np.float32(pixel_val)
criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,100,0.85)
k=int(input("enter the number of clusters(k) : "))
retval,label,centers=cv2.kmeans(pixel_val,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
centers=np.uint8(centers)
segmented_data=centers[label.flatten()]
segmented_img=segmented_data.reshape((img.shape))
plt.subplot(1,2,2)
plt.imshow(segmented_img)
plt.show()

