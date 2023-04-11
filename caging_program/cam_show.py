import cv2
import numpy as np
import matplotlib.pyplot as plt

color_img = np.load('Test_Rgb_Image.npy')
depth_img = np.load('Filtered_Depth_Image.npy')
mask_img = np.load('Maskinged_grey_after.npy')

color_img=cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)

fig = plt.figure()

#flg全体をX*Yに分割し、plot位置に画像を配置する。
X = 2
Y = 2


#imgの表示
imgplot = 1
ax1 = fig.add_subplot(X, Y, imgplot)
#タイトルの設定
ax1.set_title("color",fontsize=5)
plt.imshow(color_img)


#img2の表示
img2plot =  2
ax2 = fig.add_subplot(X, Y, img2plot)
#タイトルの設定
ax2.set_title("depth",fontsize=5)
plt.imshow(depth_img)

#img3の表示
img2plot =  4
ax2 = fig.add_subplot(X, Y, img2plot)
#タイトルの設定
ax2.set_title("mask",fontsize=5)
plt.imshow(mask_img)

plt.show() #なくても表示された。