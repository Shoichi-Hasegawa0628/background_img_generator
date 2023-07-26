import subprocess
import os
import pandas as pd
from tqdm import tqdm

topic_name = "/global_pose/pose/position"

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

# 1地点づつcsvの取得し, 保存
for i in tqdm(range(len(sorted_folder_list))):
    file_list = []
    target_path = path + "/rosbag/"+ sorted_folder_list[i]
    files = os.listdir(target_path)
    sorted_file_list = sorted(files)
    for j in range(len(sorted_file_list)):
        # print(sorted_file_list[j])
        command = ["rostopic", "echo", "-b", path + '/rosbag/{}/{}'.format(sorted_folder_list[i], sorted_file_list[j]), "-p", topic_name]
        if not os.path.exists(path + '/position/{}'.format(sorted_folder_list[i])):
            os.makedirs(path + '/position/{}'.format(sorted_folder_list[i]))
        with open(path + '/position/{}/{}.csv'.format(sorted_folder_list[i], sorted_file_list[j].replace('.bag', '')), "wb") as f:
            subprocess.run(command, stdout=f)

# position_exp.csvの作成 (6データずつ) → 180
# [living → kitchen → study_room → bedroom → bathroom → entrance] for jcmsi
# [living → kitchen → toy_room] for robocup2023
# # [living → kitchen → bedroom → bathroom] for rsj2023
order_list = ["living", "kitchen", "bedroom", "bathroom"]
for i in tqdm(range(len(order_list))):
    file_list = []
    target_path = path + "/position/"+ order_list[i]
    files = os.listdir(target_path)
    sorted_file_list = sorted(files)
    print(sorted_file_list)
    for j in range(len(sorted_file_list)):
        # 元のCSVファイルを読み込む
        df = pd.read_csv(path + "/position/{}/{}".format(order_list[i], sorted_file_list[j]), skiprows=1)
        new_df = df.iloc[0:5, 1:3]

        if i == 0 and j == 0:
            # 新規のCSVファイルに新しい行を追加する
            print(sorted_file_list[j])
            new_df.to_csv(path + "/position_exp.csv", index=False)

        else:
            # 既存のCSVファイルに新しい行を追加する
            with open(path + "/position_exp.csv", 'a') as f:
                new_df.to_csv(f, index=False)





