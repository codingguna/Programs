import cv2
img = cv2.imread('guna.jpg')
print(img.dtype)
img_neg=255-img
cv2.imshow('input',img)
cv2.imshow('negative',img_neg)
cv2.waitKey(0)
cv2.destroyAllWindows()