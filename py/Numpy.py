import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
im =Image.open('gopi.jpg')
img_arr=np.array(im)
plt.imshow(img_arr)
plt.axis("off")
plt.show()