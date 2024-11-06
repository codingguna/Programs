import numpy as np
import cv2
img=cv2.imread('download.jpeg',0)
cv2.imshow('input image',img)
f=np.fft.fft2(img)
fs=np.fft.fftshift(f)
ffs=15*np.log(1+np.abs(fs))
cv2.imshow('dft of image',np.uint8(ffs))
shift_img=np.fft.ifftshift(fs)
ifft_img=np.fft.fft2(shift_img)
abs_img=np.abs(ifft_img)
cv2.imshow('reconstructed image',np.uint8(abs_img))
cv2.waitKey(0)
cv2.destroyAllWindows()
