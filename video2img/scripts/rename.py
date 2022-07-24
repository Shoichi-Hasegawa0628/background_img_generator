#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import os

# print(sum(os.path.isfile(os.path.join("../../data/img/", name)) for name in os.listdir("../../data/img/")))
img_num = sum(os.path.isfile(os.path.join("../../data/img/", name)) for name in os.listdir("../../data/img/"))

for i in range(img_num):
    img = cv2.imread("../../data/img/{}.png".format(i))
    cv2.imwrite("../../data/rename/{}.png".format(3 + 3*i), img)





