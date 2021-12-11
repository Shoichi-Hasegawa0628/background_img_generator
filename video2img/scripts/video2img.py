#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import os

def save_4times_frames(video_path, dir_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    #base_path = os.path.join(dir_path, basename)
    #digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))
    n = 0
    while True:
        ret, frame = cap.read()
        if ret:
            if n%4 == 0:
                cv2.imwrite('./data/img/{}.png'.format(int(n/4)), frame)
            n += 1
        else:
            return

save_4times_frames('./data/video/background.mp4', './data/img')