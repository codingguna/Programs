import SimpleITK as sitk
import matplotlib.pyplot as plt

# Read the image
img = sitk.ReadImage('gopi.jpg')

# Convert the image to numpy array
img_arr = sitk.GetArrayFromImage(img)

# Display the image using matplotlib
plt.imshow(img_arr, cmap='gray')
plt.axis('off')
plt.show()