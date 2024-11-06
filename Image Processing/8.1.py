import cv2
import matplotlib.pyplot as plt

img=cv2.imread('j.png',cv2.IMREAD_GRAYSCALE)
plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('input')

ker=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
print(ker)

erosion =cv2.erode(img,ker,iterations=1)

plt.subplot(1,2,2)
plt.imshow(erosion,cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('eroded image')

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()