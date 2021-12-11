#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Standard Library
import sys

# Third Party
import rospy
import roslib.packages

# Self-made Modules
sys.path.append(str(roslib.packages.get_pkg_dir("rosbag2video")) + "/scripts")
sys.path.append(str(roslib.packages.get_pkg_dir("video2img")) + "/scripts")
import rosbag2video
import video2img


class Rosbag2Img():

    def __init__(self):
        self.converter_rosbag_to_video = rosbag2video.RosVideoWriter()
        self.converter_video_to_img = video2img.Video2Img()

    def rosbag2img(self):
        pass
        ## 構築中

if __name__ == "__main__":
    rospy.init_node('rosbag2img')
    converter_rosbag_to_img = Rosbag2Img()
    converter_rosbag_to_img.rosbag2img()
    rospy.spin()