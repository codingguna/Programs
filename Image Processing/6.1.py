import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
def dist(point1,point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
def idealfilter(d0,imgshape):
    base=np.zeros(imgshape[:2])
    rows,cols=imgshape[:2]
    center=(rows/2,cols/2)
    for i in range(cols):
        for j in range(rows):
            if dist((j,i),center)<d0:
                base[j,i]=1

    return base
fig,ax=plt.subplots(2,4)

img=cv2.imread('download.jpeg',0)
im=ax[0,0].imshow(img,cmap='gray')
ax[0,0].set_title('input image'),ax[0,0].set_xticks([]),ax[0,0].set_yticks([])

f=np.fft.fft2(img)
mag=20*np.log(np.abs(f))
im=ax[0,1].imshow(mag,cmap='gray')
ax[0,1].set_title('magnified image'),ax[0,1].set_xticks([]),ax[0,1].set_yticks([])

fshift=np.fft.fftshift(f)
mag=20*np.log(np.abs(fshift))
im=ax[0,2].imshow(mag,cmap='gray')
ax[0,2].set_title('centered spectrum'),ax[0,2].set_xticks([]),ax[0,2].set_yticks([])

im=ax[0,3].imshow(np.abs(idealfilter(50,img.shape)),cmap='gray')
ax[0,3].set_title('ideal LPF with diameter 25px')
ax[0,3].set_xticks([])
ax[0,3].set_yticks([])


im=ax[1,0].imshow(np.log(1+ np.abs(fshift*idealfilter(50,img.shape))),cmap='gray')
ax[1,0].set_title('filtered img in frequency domain')
ax[1,0].set_xticks([])
ax[1,0].set_yticks([])

im=ax[1,1].imshow(np.log(1+ np.abs(np.fft.ifftshift(fshift*idealfilter(50,img.shape)))),cmap='gray')
ax[1,1].set_title('filtered img inverse ffishift')
ax[1,1].set_xticks([])
ax[1,1].set_yticks([])


im=ax[1,2].imshow(np.log(1+ np.abs(np.fft.ifft2(np.fft.ifftshift(fshift*idealfilter(50,img.shape))))),cmap='gray')
ax[1,2].set_title('final filtered img in spatial domain')
ax[1,2].set_xticks([])
ax[1,2].set_yticks([])

ax[1,3].axis('off')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

