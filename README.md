# 'background_img_generator' Package

*   Maintainer: Shoichi Hasegawa ([hasegawa.shoichi@em.ci.ritsumei.ac.jp](mailto:hasegawa.shoichi@em.ci.ritsumei.ac.jp)).
*   Author: Shoichi Hasegawa ([hasegawa.shoichi@em.ci.ritsumei.ac.jp](mailto:hasegawa.shoichi@em.ci.ritsumei.ac.jp)).

**Content:**
*   [Requirements](#requirements)
*   [Execution](#launch)
*   [References](#references)

## Requirement

```apt
apt-get install ffmpeg
apt-get install python3-roslib python3-sensor-msgs python3-opencv
```

## Launch
1. Initialize `./reset-background-img-output.bash`  
2. Put rosbag data in /data/rosbag
3. [rosbag2video](https://github.com/Shoichi-Hasegawa0628/background_img_generator/blob/master/rosbag2video/README.md)
4. Rename video from `original name.mp4`to `background.mp4`  
5. `python /video2img/video2img.py`  





