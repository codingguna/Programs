import cv2
import matplotlib.pyplot as plt
img=cv2.imread('download.jpeg',cv2.IMREAD_GRAYSCALE)
plt.hist(img.flatten(),256,[0,256])
cv2.imshow('input img',img)
plt.xlabel('gray level')
plt.ylabel('number of pixel')
plt.title('histogram using matplotlib')
plt.show()
histr=cv2.calcHist([img],[0],None,[256],[0,256])
p1=plt.plot(histr)
plt.xlabel('gray level')
plt.ylabel("number of pixel")
plt.title('histogram using opencv')
plt.show()
cv2.normalize(histr,histr,0,1,cv2.NORM_MINMAX)
plt.plot(histr)
plt.xlabel('gray level')
plt.ylabel('number fo pixels')
plt.title('normalized histogram using opencv')
cv2.waitKey(0)
cv2.destroyAllWindows()


