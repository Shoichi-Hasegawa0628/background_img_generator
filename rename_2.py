#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import os


img_path = "/root/HSR/datasets/irex2022_object/objects/irex2022_001_toiletries/rgb"
# img_path = "/root/HSR/catkin_ws/src/spco_dataset_generator/data/output/test/image/kitchen/raw"
# print(sum(os.path.isfile(os.path.join(img_path, name)) for name in os.listdir(img_path)))
img_num = sum(os.path.isfile(os.path.join(img_path, name)) for name in os.listdir(img_path))
files = os.listdir(img_path)
file_names = [f for f in files if os.path.isfile(os.path.join(img_path, f))]
# print(file_names)

for i in range(img_num):
    # img = cv2.imread(img_path + "/{}".format(file_names[i]))
    img = cv2.imread(img_path + "/rgb_{}.png".format(i), -1)
    cv2.imwrite("/root/HSR/datasets/irex2022_object/objects/irex2022_001_toiletries/rename" + "/rgb_{}.png".format(i), img)
    # cv2.imwrite(img_path + "/rename" + "/{}.jpg".format(i + 1), img)


# first = [0, 30, 60, 300, 330]
# second = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
#
# for i in range(len(first)):
#     for j in range(len(second)):
#         # img = cv2.imread(img_path + "/{}".format(file_names[i]))
#         img = cv2.imread(img_path + "/mask_{}_{}_0.png".format(first[i], second[j]))
#         if i == 0:
#             cv2.imwrite("/root/HSR/catkin_ws/src/background_img_generator/data/irex_cup/mask/rename" + "/rgb_{}.png".format(2 + i + j), img)
#         if i == 1:
#             cv2.imwrite("/root/HSR/catkin_ws/src/background_img_generator/data/irex_cup/mask/rename" + "/rgb_{}.png".format(13 + i + j), img)
#         if i == 2:
#             cv2.imwrite("/root/HSR/catkin_ws/src/background_img_generator/data/irex_cup/mask/rename" + "/rgb_{}.png".format(24 + i + j), img)
#         if i == 3:
#             cv2.imwrite("/root/HSR/catkin_ws/src/background_img_generator/data/irex_cup/mask/rename" + "/rgb_{}.png".format(35 + i + j), img)
#         else:
#             cv2.imwrite("/root/HSR/catkin_ws/src/background_img_generator/data/irex_cup/rgb/rename" + "/rgb_{}.png".format(47 + i + j), img)
#         # cv2.imwrite(img_path + "/rename" + "/{}.jpg".format(i + 1), img)




