import numpy as np 
import ikpy
import matplotlib.pyplot as plt
from math import pi 

irb120 = ikpy.chain.Chain.from_urdf_file('robot.URDF',base_elements=['base_link'])
print(type(irb120))
home_joints = np.array([0,0,0,0,0,0])

home_trans = np.array([[-1, 0, 0, 0.374],
						[0, 1, 0, 0],
						[0, 0, -1, 0.630],
						[0, 0, 0, 1]])



joint_angles = irb120.inverse_kinematics(home_trans)

print(joint_angles)

test_joints = np.array([0, 0, 0, 0, 0, 0, pi/2])

test_ik = irb120.forward_kinematics(joint_angles)


# end_effector = irb120.forward_kinematics(test_joints)

print(test_ik)

