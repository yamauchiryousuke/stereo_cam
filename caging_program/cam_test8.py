# すべてのデータ読み込み

# -*- coding: utf-8 -*-
#matplotlib inline
import pyrealsense2 as rs
import numpy as np
import cv2
import matplotlib.pyplot as plt
import open3d as o3d
# ストリーム(Color/Depth)の設定
config = rs.config()
align = rs.align(rs.stream.color)

config.enable_stream(rs.stream.infrared, 1, 640, 480, rs.format.y8, 30)
config.enable_stream(rs.stream.infrared, 2, 640, 480, rs.format.y8, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8,30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_device_from_file('color_640_480_d435idata.bag')#color_640_480_d435idata.bag

# ストリーミング開始
pipeline = rs.pipeline()
profile = pipeline.start(config)
depth_sensor = profile.get_device().first_depth_sensor()
depth_scale = depth_sensor.get_depth_scale()

print("Depth Scale is: " , depth_scale)

clipping_distance_in_meters = 1 #1 meter
clipping_distance = clipping_distance_in_meters / depth_scale
intr = profile.get_stream(rs.stream.color).as_video_stream_profile().get_intrinsics()
pinhole_camera_intrinsic = o3d.camera.PinholeCameraIntrinsic(intr.width, intr.height, intr.fx, intr.fy, intr.ppx, intr.ppy)

# decimarion_filterのパラメータ
decimate = rs.decimation_filter()
decimate.set_option(rs.option.filter_magnitude, 1)
# spatial_filterのパラメータ
spatial = rs.spatial_filter()
spatial.set_option(rs.option.filter_magnitude, 1)
spatial.set_option(rs.option.filter_smooth_alpha, 0.25)
spatial.set_option(rs.option.filter_smooth_delta, 50)
# hole_filling_filterのパラメータ
hole_filling = rs.hole_filling_filter()
# disparity
depth_to_disparity = rs.disparity_transform(True)
disparity_to_depth = rs.disparity_transform(False)

try:
    while True:
        
        # フレーム待ち(Color & Depth)
        frames = pipeline.wait_for_frames() #frameのデータを所得
        aligned_frames = align.process(frames)
        
        color_frame = aligned_frames.get_color_frame() #RGBのframeデータを所得
        depth_frame = aligned_frames.get_depth_frame() #Depthのframeデータを所得
        if not depth_frame or not color_frame: #どちらかを所得出来ない場合，無限ループ
            continue
        
        filter_frame = decimate.process(depth_frame)
        filter_frame = depth_to_disparity.process(filter_frame)
        filter_frame = spatial.process(filter_frame)
        filter_frame = disparity_to_depth.process(filter_frame)
        filter_frame = hole_filling.process(filter_frame)
        depth_frame = filter_frame.as_depth_frame()
        
        color_image = np.asanyarray(color_frame.get_data()) # Bafデータを所得し配列に変換　(RGB)
        depth_image = np.asanyarray(depth_frame.get_data())
        
        depth_color_frame = rs.colorizer().colorize(depth_frame)
        depth_color_image = np.asanyarray(depth_color_frame.get_data()) 
        images = np.hstack((color_image, depth_color_image)) #２画面に変換

        

     # 表示
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', images)
        if cv2.waitKey(1) & 0xff == 27:
            cv2.destroyAllWindows()
            break
            
finally:
    pipeline.stop()
    img_test=cv2.cvtColor(images, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(20,20), dpi=100 ) #表示される画像自体の大きさを変更，dpiは解像度の変更
    plt.subplot(1, 1, 1)
    plt.grid(False)
    plt.rcParams["font.size"] =20 #titleの文字サイズの大きさ変更
    plt.title('RGB_Image and RGB-D_Image') #タイトル名    plt.tick_params(labelsize=30) #メモリ自体の文字サイズの大きさ変更
    plt.imshow(img_test)

    Rgb_Image = color_image
    filtered_depth_image = depth_color_image
    np.save("Test_Rgb_Image" ,Rgb_Image)
    np.save("Filtered_Depth_Image",filtered_depth_image)