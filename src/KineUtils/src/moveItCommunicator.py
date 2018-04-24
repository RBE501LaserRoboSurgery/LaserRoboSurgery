import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from utils import *
import cPickle as pickle
from Config import *
from std_msgs.msg import String


# Global variables
robot = []
scene = []
group = []
display_trajectory_publisher = []


def initCommunicator():

	global robot, scene, group

	print("============ Starting setup ============ ")
	moveit_commander.roscpp_initialize(sys.argv)
	rospy.init_node('move_group_python_interface_tutorial', anonymous = True)

	# Instantiate a RobotCommander object.  This object is an interface to
	# the robot as a whole.
	robot = moveit_commander.RobotCommander()

	## Instantiate a PlanningSceneInterface object.  This object is an interface
	## to the world surrounding the robot.
	scene = moveit_commander.PlanningSceneInterface()

	## Instantiate a MoveGroupCommander object.  This object is an interface
	## to one group of joints.  In this case the group is the joints in the left
	## arm.  This interface can be used to plan and execute motions on the left
	## arm.
	group = moveit_commander.MoveGroupCommander("manipulator")


	## We create this DisplayTrajectory publisher which is used below to publish
	## trajectories for RVIZ to visualize.
	display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

	## Wait for RVIZ to initialize. This sleep is ONLY to allow Rviz to come up.
	# print "============ Waiting for RVIZ..."
	rospy.sleep(1)

	print("MoveIt Communicator initialized")


def stopCommunicator():
	## When finished shut down moveit_commander.
	moveit_commander.roscpp_shutdown()


### Checks if the desired pt lies in config space
def checkValidPoint(pt):
	x = pt[0]
	y = pt[1]
	z = pt[2]
	assert x**2+y**2+(z-.290)**2 >= 0.17*0.17
	assert m.atan2(y,x) > -165*m.pi/180 and m.atan2(y,x) < 165*m.pi/180
	# assert (m.sqrt(x**2+y**2)-0.25)**2+(z-0.29)**2>=0.098596


### Moves end effector to desired pt at orientation angs
def goToPoint(pt, angs = default_angs):
	global group	
	# checkValidPoint(pt)
	try:
		pose_target = geometry_msgs.msg.Pose()
		oQs = convertE2Q([angs[0], angs[1], angs[2]])
		pose_target.orientation.w = oQs[3]
		pose_target.orientation.x = oQs[0]
		pose_target.orientation.y = oQs[1]
		pose_target.orientation.z = oQs[2]
		pose_target.position.x = pt[0]
		pose_target.position.y = pt[1]
		pose_target.position.z = pt[2]
		group.set_pose_target(pose_target)
		plan1 = group.plan()
		group.execute(plan1)

		rospy.sleep(2)
	except:
		pass

def goToWaypoints(waypoints, angs = default_angs):
	for pt in waypoints:
		goToPoint(pt, angs)
		

def goHome():
	goToPoint(HOME_POS['pts'], HOME_POS['angs'])
	print("Going to Home Position")

def goLaserHome():
	goToPoint(HOME_LASER_POS['pts'], HOME_LASER_POS['angs'])
	print("Going to Laser Home Position")


def testInterface():

	initCommunicator()

	print("============ Going to home ============")
	goHome()


	print("============ Square Waypoint Trajectory ============")
	goToWaypoints(TEST_SQUARE)


# if __name__=='__main__':
# 	try:
# 		testInterface()
# 	except rospy.ROSInterruptException:
# 		pass