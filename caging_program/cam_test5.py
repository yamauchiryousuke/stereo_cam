import numpy as np
import matplotlib.pyplot as plt
import cv2

Rgb_Image = np.load('Test_Rgb_Image.npy')

plt.figure(figsize=(20,20), dpi=100 ) #表示される画像自体の大きさを変更，dpiは解像度の変更
plt.subplot(1, 1, 1)
plt.grid(False)
plt.rcParams["font.size"] =20 #titleの文字サイズの大きさ変更
plt.title('Depth_Image') #タイトル名
plt.tick_params(labelsize=20)#メモリ自体の文字サイズの大きさ変更
Rgb_Image=cv2.cvtColor(Rgb_Image, cv2.COLOR_BGR2RGB)
plt.imshow(Rgb_Image)
plt.show()