import cv2
import matplotlib.pyplot as plt

img=cv2.imread('j2.bmp',cv2.IMREAD_GRAYSCALE)
plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('input')

ker=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
print(ker)

dilat=cv2.dilate(img,ker,iterations=1)
closing =cv2.erode(dilat,ker,iterations=1)

plt.subplot(1,2,2)
plt.imshow(closing,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('closing')

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()