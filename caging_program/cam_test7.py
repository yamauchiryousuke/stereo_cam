import pyrealsense2 as rs
import matplotlib.pyplot as plt
import numpy as np

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
depth_to_desparity = rs.disparity_transform(True)
desparity_to_depth = rs.disparity_transform(False)

#frame取得
depth_frame = np.load('depth_frame.npy')

# filterをかける
filter_frame = decimate.process(depth_frame)
filter_frame = depth_to_desparity.process(filter_frame)
filter_frame = spatial.process(filter_frame)
filter_frame = disparity_to_depth.process(filter_frame)
filter_frame = hole_filling.process(filter_frame)

result_frame = filter_frame.as_depth_frame()
filtered_depth_image = np.asanyarray(result_frame.get_date())

plt.figure(figsize=(10,10), dpi=100 ) #表示される画像自体の大きさを変更，dpiは解像度の変更
plt.subplot(1, 1, 1)
plt.grid(False)
plt.rcParams["font.size"] =20 #titleの文字サイズの大きさ変更
plt.title('RGB_Image and RGB-D_Image') #タイトル名    plt.tick_params(labelsize=30) #メモリ自体の文字サイズの大きさ変更
plt.tick_params(labelsize=20)
plt.imshow(img_test)
plt.show()
np.save("Filtered_Depth_Image",filtered_depth_image)