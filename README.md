# Welcome to LaserRoboSurgery

## Setup ##
1. git clone https://github.com/RBE501LaserRoboSurgery/LaserRoboSurgery
2. cd into the cloned repo and run `catkin_make` 

Note: Built and tested on ROS Kinetic; For ROS Indigo, delete CMakeList.txt and `catkin_make` 

3. In your `.bashrc` file you need to add the line `source /path/to/solder_paste_workspace/devel/setup.bash` anywhere in the file. `/path/to` being the path to wherever you placed the workspace. I would also reccomend adding this line:
	`alias bashupdate="source ~/.bashrc"`
		This allows you to run the command `bashupdate` which will re-source your `.bashrc` file. This is especially important when you make new packages or executables, otherwise they won't show up in `rosrun` or `roslaunch` without first closing and reopening your terminal. This just lets you skip that step.


## Launching ROS NODES  and connecting to robot ##

1. Connect Robot Studio with ROS
roslaunch abb_irb120_support robot_interface_download_irb120.launch robot_ip:=ip_address
my address is 192.168.1.102

2. Launch moveit planning execution and don't run the following commands if you just want to see how it works
roslaunch abb_irb120_moveit_config moveit_planning_execution.launch

3. Or Launch move group if you want to control the robot by your code
roslaunch abb_irb120_moveit_config move_group.launch

4. Run the robot
rosrun moveit_nodes move_group_interface
In rviz, choose Key Tool and click 'n' in keyboard for next step.
After running this, you can see the robot moves to several poses.


## Launcing GUI ##
1. Connect to the robot ast mentioned in the above step.

2. Connect the camera to the commanding system. Ensure that the workspace is visible in camera frame. Ensure that the camera is mapped to /dev/video1.

3. Now from root of this repository, launch the GUI by:
	$ python src/KineUtils/src/laserGUI.py

4. A Window will open displaying the current view from camera. In the frame, select (by mouse left-doubleclick) the 4 corner points of the workspace starting from top left and going clockwise.
	The points can be cleared by clicking 'c' at any time.
	The points can be finalized by clicking 'd'

5. Once the points are registered, a new window will open showing a top view of the workspace. The trajectories can now be drawn on the frame by the mouse (either by double click or by scribbling(click and drag)). The keyboard hotkeys are:
```
		m: Toggle drawing mode
		d: Finilize drawn points and start moving end effector accordingly.
		c: Clear drawn points. Stop current execution
		q: Quit program
```

6. The finalized points will be forwarded to the moveIt! planner and to the robot.
