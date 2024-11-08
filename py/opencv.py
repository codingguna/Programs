import cv2
import matplotlib.pyplot as plt
img=cv2.imread('gopi.jpg')
im_rgb=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
plt.imshow(im_rgb)
plt.axis('off')
plt.show()