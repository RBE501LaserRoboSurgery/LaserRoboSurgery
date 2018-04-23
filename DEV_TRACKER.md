### DEV TRACKER FOR LASER ROBOT SURGERY ###
Current version: 0.0.3
Date Modified: 2018-04-23 (YYYY-MM-DD)

## Changes in version 0.0.2 ##
	Changes:
		Additional support for manipulating points from camera frame to world frame.
		Now scribble mode is supported to enter trajectory points.
		The hotkeys are:
			m: Toggle drawing mode
			d: Finilize drawn points and start moving end effector accordingly.
			c: Clear drawn points. Stop current execution
			q: Quit program  


## Changes in version 0.0.2 ##
	Changes:
		Multithreading support for separate renderGUI thread and moveit thread.

## Changes in version 0.0.1 ##
	Added files:
		laserGUI.py
	Changes:
		First commit of GUI of the project.
		laserGUI.py is the basic GUI which takes in mouse clicks for trajectory planning.
		The clicked points are registered by clicking 'd'.
		The program exits by pressing 'q'.
