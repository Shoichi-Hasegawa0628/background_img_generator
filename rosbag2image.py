import subprocess
import os
import pandas as pd
from tqdm import tqdm

topic_name = "/hsrb/head_rgbd_sensor/rgb/image_rect_color/compressed"

# パスの取得
result = subprocess.run(['pwd'], stdout=subprocess.PIPE)
output = result.stdout.strip().decode()
path = output + '/data'

# フォルダの数をカウント
folder_list = []
folders = os.listdir(path + '/rosbag')
for folder in folders:
    if os.path.isdir(os.path.join(path + '/rosbag', folder)):
        folder_list.append(folder)
        # print(folder_list)
sorted_folder_list = sorted(folder_list)

# 1地点づつmp4と画像を取得し, 保存
for i in tqdm(range(len(sorted_folder_list))):
    file_list = []
    target_path = path + "/rosbag/"+ sorted_folder_list[i]
    files = os.listdir(target_path)
    sorted_file_list = sorted(files)
    for j in tqdm(range(len(sorted_file_list))):
        # print(sorted_file_list[j])
        # Start rosbag2video.py using subprocess
        rosbag2video_process = subprocess.Popen(['python3',
                                                 "/root/HSR/catkin_ws/src/background_img_generator/rosbag2video/scripts/rosbag2video.py",
                                                 '--fps', '30',
                                                 '-t',
                                                 topic_name,
                                                 '-o',
                                                 path + '/video/{}/{}.mp4'.format(sorted_folder_list[i], sorted_file_list[j].replace(".bag", "")),
                                                 path + '/rosbag/{}/{}'.format(sorted_folder_list[i], sorted_file_list[j])]) # bag → video

        if not os.path.exists(path + '/image/{}/{}'.format(sorted_folder_list[i], str(j + 1))):
            os.makedirs(path + '/image/{}/{}'.format(sorted_folder_list[i], str(j + 1)))

        video2img_process = subprocess.Popen(['python3',
                                              "/root/HSR/catkin_ws/src/background_img_generator/video2img/scripts/video2img.py",
                                              path + '/video/{}/{}.mp4'.format(sorted_folder_list[i], sorted_file_list[j].replace(".bag", "")),
                                              path + '/image/{}/{}'.format(sorted_folder_list[i], str(j + 1))]) # video → image





