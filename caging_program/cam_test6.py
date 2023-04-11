import cv2
import numpy as np
from IPython.display import Image, display
from ipywidgets import widgets

def imshow(img):
    ret, encoded = cv2.imencode(".png",img)
    display(Image(encoded))

def inRange(**kwarge):
    lower = tuple([int(l) for l,h in kwarge.values()])
    upper = tuple([int(l) for l,h in kwarge.values()])
    binary = cv2.inRange(img, lowerb=lower, upperb=upper)
    imshow(binary)

Color_Image = np.load('Test_Rgb_image.npy')
color_img = cv2.cvtColor(Color_Image, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(color_img, cv2.COLOR_BGR2HSV)

num_channels = 1 if img.ndim == 2 else img.shape[2]
parts = {}

for i in range(num_channels):
    slider = widgets.SelectionRangeSlider(
        options=np.arange(256), index=(0,255), descrioption=f"channel {i}"
    )
    slider.layout.width = "480px"
    parts[f"channel{i}"] = slider

widgets.interactive(inRange, **parts)