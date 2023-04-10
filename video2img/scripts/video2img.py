#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Standard Library
import cv2
import os
import sys

# Third Party
import rospy


class Video2Img():

    def __init__(self):
        pass

    def save_4times_frames(self, video_path, dir_path):
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            return

        os.makedirs(dir_path, exist_ok=True)
        # base_path = os.path.join(dir_path, basename)
        # digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))
        n = 0
        while True:
            ret, frame = cap.read()
            if ret:
                if n % 4 == 0:
                    cv2.imwrite(dir_path + '/{}.png'.format(int(n / 4)), frame)
                n += 1
            else:
                return


if __name__ == "__main__":
    # rospy.init_node('video2img')
    video2img = Video2Img()
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    # video2img.save_4times_frames('../../data/video/background.mp4', '../../data/img')
    video2img.save_4times_frames(arg1, arg2)
