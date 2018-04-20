# Welcome to LaserRoboSurgery

## Setup
* Clone
* cd into the cloned repo and `catkin_make` 

Note: Built and tested on ROS Kinetic; For ROS Indigo, delete CMakeList.txt and `catkin_make` 


Bug fixes
pythoncv conflicts with ros opencv because the ROS setup.bash sets  PYTHONPATH to point to its location.
Solution: add unset PYTHONPATH to your .bashrc file after calling ROS setup.bash
