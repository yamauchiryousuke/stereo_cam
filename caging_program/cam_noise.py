import cv2
import numpy as np
import matplotlib.pyplot as plt

img_mask = np.load('Test_Mask_Image.npy')

kernel = np.ones((9,9),np.uint8)
closing = cv2.morphologyEx(img_mask,cv2.MORPH_CLOSE,kernel)
opening = cv2.morphologyEx(img_mask,cv2.MORPH_OPEN,kernel)
maskinged_grey_image = cv2.cvtColor(opening,cv2.COLOR_BGR2RGB)

plt.figure(figsize=(20,20))
plt.subplot(1,1,1)
plt.grid(False)
plt.rcParams["font.size"] = 20
plt.tick_params(labelsize=20)
plt.imshow(maskinged_grey_image)
plt.show()

np.save("Maskinged_grey_after",maskinged_grey_image)