import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
#img = np.zeros((300,512,3), np.uint8)
#Color_Image = np.load('Test_Rgb_Image.npy')
color_img = np.load('Test_Rgb_Image.npy')
#color_img = cv2.cvtColor(Color_Image, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(color_img, cv2.COLOR_BGR2HSV)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('H_U','image',0,255,nothing)
cv2.createTrackbar('H_L','image',0,255,nothing)
cv2.createTrackbar('S_U','image',0,255,nothing)
cv2.createTrackbar('S_L','image',0,255,nothing)
cv2.createTrackbar('V_U','image',0,255,nothing)
cv2.createTrackbar('V_L','image',0,255,nothing)

while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    h_u = cv2.getTrackbarPos('H_U','image')
    h_l = cv2.getTrackbarPos('H_L','image')
    s_u = cv2.getTrackbarPos('S_U','image')
    s_l = cv2.getTrackbarPos('S_L','image')
    v_u = cv2.getTrackbarPos('V_U','image')
    v_l = cv2.getTrackbarPos('V_L','image')

    lower = np.array([h_l,s_l,v_l])
    upper = np.array([h_u,s_u,v_u])

    mask = cv2.inRange(img, lower, upper)

    cv2.imshow('image',mask)


cv2.destroyAllWindows()
np.save("Test_Mask_Image",mask)