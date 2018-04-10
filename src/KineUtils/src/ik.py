import numpy as np
from jacob import Jacobian
# import ikpy
import pdb
import time

class IK:
	global lamda
	lamda=0.00001
	def __init__(self,robot):
 		self.robot=robot
 		# self.chain = robot.urdf

	def NewtonIK(self,xf,qi=None):#pass
 		return (self.robot.urdf.inverse_kinematics([[1, 0, 0, xf[0]],
                             [0, 1, 0, xf[1]],
                             [0, 0, 1, xf[2]],
                             [0, 0, 0, 1]]))

	def IterJInv(self,xf,qi=None):
		st=time.time()
 		if qi is None:
 			qi=np.zeros([len(self.robot.rho),1])

 		J=Jacobian(self.robot.dh,self.robot.rho)

 		Jpinv=np.transpose(J)
 		while np.abs(np.linalg.norm(np.dot(J,qi)-xf))>1e-5:
 			self.robot.calcDH(qi)
 			J=Jacobian(self.robot.dh,self.robot.rho)
 			Jpinv=np.dot(np.transpose(J),np.linalg.inv((lamda**2)*np.identity(6)+np.dot(J,np.transpose(J))))
 			# Jpinv=np.transpose(J)
 			# print(Jpinv)
 			Jg=np.dot(Jpinv,(xf-np.dot(J,qi)).reshape(6,1))
 			qi+=0.001*Jg
 			# print(np.linalg.norm(np.dot(J,qi)-xf))
 		print('IK solved in '+str(time.time()-st))
 		return qi

	def CCD(self,xf,qi):
 		pass
