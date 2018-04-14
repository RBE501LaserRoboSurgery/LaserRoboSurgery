import rospy
import csv
from trajectory_msgs.msg import JointTrajectory
from factory import robot
import rospy
from threading import *
import time as t
import math as m
import string
import keyboard
from pynput import keyboard
from traj_primitives import *

t0=t.time()
TRAJ_TYPES={'Straight':1,'Arc':2,'S':3}

Robot=None
traj_pts=[]

class rosact(object):
	def __init__(self):
		rospy.init_node('act')
		self.pubs=[]
		self.pubs.append(rospy.Publisher('/irb120/joint_1_position_controller/command',Float64,queue_size=10))
		self.pubs.append(rospy.Publisher('/irb120/joint_2_position_controller/command',Float64,queue_size=10))
		self.pubs.append(rospy.Publisher('/irb120/joint_3_position_controller/command',Float64,queue_size=10))
		self.pubs.append(rospy.Publisher('/irb120/joint_4_position_controller/command',Float64,queue_size=10))
		self.pubs.append(rospy.Publisher('/irb120/joint_5_position_controller/command',Float64,queue_size=10))
		self.pubs.append(rospy.Publisher('/irb120/joint_6_position_controller/command',Float64,queue_size=10))
		rospy.sleep(1)

	def write(self,rob,pos=None):
		traj_start=time.time()

		for p in traj_pts:
			
			p=p.split(',')
			p=[float(i) for i in p]
			######   Call IK    ######
			# pos=rob.IK_bfgs(pts)
			
			msg=Float64() 
			print('Writing '+ str(pos))
			for i in range(len(pos)):
				msg.data=pos[i]
				self.pubs[i].publish(msg)
		print('Trajectory exxecution time= '+str(time.time()-traj_start))


def run():
	Robot=robot()
	Robot.BuildKineModules()
	
	###### Test FK ######
	# a=Robot.GetEffectorPosition(jts)
	# print('final pos')
	# print(a)

	# print(Robot.SetEffectorPosition(a)*180/m.pi)

	act=rosact()
	# act.write(Robot)
	print('this shouldnt be displayed')

if __name__== '__main__':
	print('Select trajectory')
	print('1: Straight      2: Arc      3: S')
	selected_traj=input()

	###  Generate/ Fetch points  ###
	traj=TrajGenerator(selected_traj)

	print('Press t to track the selected trajectory')
	while True:#making a loop
	    try: #used try so that if user pressed other than the given key error will not be shown
	        if keyboard.is_pressed('t'):#if key 'q' is pressed 
	            run()
	            break#finishing the loop
	        else:
	            pass
	    except:
	        break #if user pressed other than the given key the loop will break

