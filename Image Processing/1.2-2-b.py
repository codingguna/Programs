import cv2 
img = cv2.imread('download.jpeg', cv2.IMREAD_UNCHANGED) 
print('Original Dimensions : ',img.shape) 
scale_percent = 60
width = int(img.shape[1] * scale_percent / 100) 
height = int(img.shape[0] * scale_percent / 100) 
dim = (width, height)  
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) 
print('Resized Dimensions : ',resized.shape) 
cv2.imshow("Resized image", resized) 
cv2.waitKey(0) 
cv2.destroyAllWindows()