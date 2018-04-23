import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from utils import *
import cPickle as pickle
from Config import *
## This script is modified from the original script found here: 

from std_msgs.msg import String

def move_group_python_interface_tutorial():
	


	### Resets the arm to home position
	def go_home(group):
		pose_target = geometry_msgs.msg.Pose()
		oQs=convertE2Q(HOME_POS['angs'])
		pose_target.orientation.w = oQs[3]
		pose_target.orientation.x=oQs[0]
		pose_target.orientation.y=oQs[1]
		pose_target.orientation.z=oQs[2]
		pose_target.position.x = HOME_POS['pts'][0]
		pose_target.position.y = HOME_POS['pts'][1]
		pose_target.position.z = HOME_POS['pts'][2]
		group.set_pose_target(pose_target)
		plan1 = group.plan()
		group.execute(plan1)

	# print "============ Starting setup"
	moveit_commander.roscpp_initialize(sys.argv)
	rospy.init_node('move_group_python_interface_tutorial',
				  anonymous=True)

	## Instantiate a RobotCommander object.  This object is an interface to
	## the robot as a whole.
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
	display_trajectory_publisher = rospy.Publisher(
									  '/move_group/display_planned_path',
									  moveit_msgs.msg.DisplayTrajectory)

	## Wait for RVIZ to initialize. This sleep is ONLY to allow Rviz to come up.
	# print "============ Waiting for RVIZ..."
	rospy.sleep(10)

	## Getting Basic Information
	## ^^^^^^^^^^^^^^^^^^^^^^^^^
	##
	## We can get the name of the reference frame for this robot
	# print "============ Reference frame: %s" % group.get_planning_frame()

	## We can also print the name of the end-effector link for this group
	# print "============ Reference frame: %s" % group.get_end_effector_link()

	## We can get a list of all the groups in the robot
	# print "============ Robot Groups:"
	# print robot.get_group_names()

	## Sometimes for debugging it is useful to print the entire state of the
	## robot.
	# print "============ Resetting to home"
	go_home(group)
	rospy.sleep(10)
	# print "============ Deploy Laser"
	go_to_point(group,DEPLOY_LASER['pts'],DEPLOY_LASER['angs'])
	rospy.sleep(30)
	# config_home= robot.get_current_state()
	# print(config_home)

	# try:
	# 	config_home = pickle.load(open("home.p", "rb"))
	# except (OSError, IOError) as e:
	# 	pickle_out = open("home.p","wb")
	# 	pickle.dump(config_home, pickle_out)
	# 	pickle_out.close()
	# print "============ Initial pose"
	# print(config_home.joint_state.position)
	# print(group.get_current_pose())

	## Planning to a Pose goal
	## ^^^^^^^^^^^^^^^^^^^^^^^
	## We can plan a motion for this group to a desired pose for the 
	## end-effector
	# print "============ Generating plan 1"
	
	

	# ## Now, we call the planner to compute the plan
	# ## and visualize it if successful
	# ## Note that we are just planning, not asking move_group 
	# ## to actually move the robot

	## You can ask RVIZ to visualize a plan (aka trajectory) for you.  But the
	## group.plan() method does this automatically so this is not that useful
	## here (it just displays the same trajectory again).

	# print "============ Visualizing plan1"
	# display_trajectory = moveit_msgs.msg.DisplayTrajectory()

	# display_trajectory.trajectory_start = robot.get_current_state()
	# display_trajectory.trajectory.append(plan1)
	# display_trajectory_publisher.publish(display_trajectory);

	# print "============ Waiting while plan1 is visualized (again)..."
	# rospy.sleep(5)


	## Moving to a pose goal
	## ^^^^^^^^^^^^^^^^^^^^^
	##
	## Moving to a pose goal is similar to the step above
	## except we now use the go() function. Note that
	## the pose goal we had set earlier is still active 
	## and so the robot will try to move to that goal. We will
	## not use that function in this tutorial since it is 
	## a blocking function and requires a controller to be active
	## and report success on execution of a trajectory.

	# Uncomment below line when working with a real robot
	# group.go(wait=True)

	## Planning to a joint-space goal 
	## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	##
	## Let's set a joint space goal and move towards it. 
	## First, we will clear the pose target we had just set.

	# group.clear_pose_targets()

	# ## Then, we will get the current set of joint values for the group
	# group_variable_values = group.get_current_joint_values()
	# print "============ Joint values: ", group_variable_values

	# ## Now, let's modify one of the joints, plan to the new joint
	# ## space goal and visualize the plan
	# group_variable_values[0] = 1.0
	# group.set_joint_value_target(group_variable_values)

	# plan2 = group.plan()

	## Cartesian Paths
	## ^^^^^^^^^^^^^^^
	## You can plan a cartesian path directly by specifying a list of waypoints 
	## for the end-effector to go through.

	for pt in TEST_SQUARE['pts']:
		go_to_point(group,pt,TEST_SQUARE['angs'])
		rospy.sleep(30)
		
	# rospy.sleep(5)
	# follow_points(group,TEST_LINE['pts'],TEST_LINE['angs'])
	rospy.sleep(10)

	## Adding/Removing Objects and Attaching/Detaching Objects
	## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	## First, we will define the collision object message
	collision_object = moveit_msgs.msg.CollisionObject()

	## When finished shut down moveit_commander.
	moveit_commander.roscpp_shutdown()

	# print "============ STOPPING"

def follow_points(group,pts,angs):
	waypoints = []

	# start with the current pose
	waypoints.append(group.get_current_pose().pose)

	# first orient gripper and move forward (+x)
	pose_target = geometry_msgs.msg.Pose()
	group.clear_pose_targets()
	try:
		for pt in pts:
			pose_target = geometry_msgs.msg.Pose()
			oQs=convertE2Q([angs[0],angs[1],angs[2]])
			pose_target.orientation.w = oQs[3]
			pose_target.orientation.x=oQs[0]
			pose_target.orientation.y=oQs[1]
			pose_target.orientation.z=oQs[2]
			pose_target.position.x = pt[0]
			pose_target.position.y = pt[1]
			pose_target.position.z = pt[2]
			waypoints.append(copy.deepcopy(pose_target))
		(plan, fraction) = group.compute_cartesian_path(
							   waypoints,   # waypoints to follow
							   0.01,        # eef_step
							   0.0)         # jump_threshold
		group.execute(plan)
	except:
		pass


### Moves end effector to desired pt at orientation angs
def go_to_point(group,pt,angs):
	in_robot_range(pt)
	try:
		pose_target = geometry_msgs.msg.Pose()
		oQs=convertE2Q([angs[0],angs[1],angs[2]])
		pose_target.orientation.w = oQs[3]
		pose_target.orientation.x=oQs[0]
		pose_target.orientation.y=oQs[1]
		pose_target.orientation.z=oQs[2]
		pose_target.position.x = pt[0]
		pose_target.position.y = pt[1]
		pose_target.position.z = pt[2]
		group.set_pose_target(pose_target)
		plan1 = group.plan()
		group.execute(plan1)
	except:
		pass

### Checks if the desired pt lies in config space
def in_robot_range(pt):
	x=pt[0]
	y=pt[1]
	z=pt[2]
	assert x**2+y**2+(z-.290)**2>=0.17*0.17
	assert m.atan2(y,x)>-165*m.pi/180 and m.atan2(y,x)<165*m.pi/180
	# assert (m.sqrt(x**2+y**2)-0.25)**2+(z-0.29)**2>=0.098596



if __name__=='__main__':
	try:
		move_group_python_interface_tutorial()
	except rospy.ROSInterruptException:
		pass