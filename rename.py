#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import os

img_path = "/root/HSR/background_img/living/img"
# print(sum(os.path.isfile(os.path.join(img_path, name)) for name in os.listdir(img_path)))
img_num = sum(os.path.isfile(os.path.join(img_path, name)) for name in os.listdir(img_path))

for i in range(img_num):
    img = cv2.imread(img_path + "/{}.png".format(i))
    cv2.imwrite(img_path + "/{}.png".format(604 + (i + 1)), img)




