import cv2
img=cv2.imread("download.jpeg")
cv2.imshow('my Display',img)
cv2.waitKey(0)
cv2.destroyAllWindows()