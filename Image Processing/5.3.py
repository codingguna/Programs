import pywt
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('download.jpeg',0)
coeff=pywt.dwt2(img,'bior1.3')
cA,(cH,cV,cD)=coeff
plt.subplot(121),plt.imshow(cA,cmap='gray')
plt.title('approximate coefficient'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(cH,cmap='gray')
plt.title('horizontal coefficient'),plt.xticks([]),plt.yticks([])
plt.show()
img_recon=pywt.idwt2(coeff,'bior1.3')
plt.imshow(img_recon,cmap='gray')
plt.title('reconstructed image'),plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()