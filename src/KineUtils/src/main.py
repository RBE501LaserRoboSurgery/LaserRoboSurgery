from factory import robot
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Bool
from geometry_msgs.msg import Point
import time as t
import math as m
t0=t.time()
Robot=None
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
        traj_st=time.time()

        while True:
            pts=traj_pnt('square',traj_st,pts)
            pos=rob.IK_bfgs(pts)
            pos=pos[1:]
            print(pos)
            #pos=[0]*6
            #pos[4]=m.pi/2
            # pos[3]=0
            # pos[4]=0
            # pos[5]=m.pi/2
            msg=Float64() 
            print('Writing ')
            print(pos)
            for i in range(len(pos)):
                msg.data=pos[i]+(t.time()-t0)/180 if i==4 else pos[i]
                self.pubs[i].publish(msg)
            #rospy.sleep(0.01)
    
    # def traj_pnt(tr_type,tm,st,vel=0.1,**kwargs):
    #     t=time.time()
    #     assert type(tr_type) is str
    #     if type.lower()=='square':
    #         if st+vel*((t-tm)%` )>kwargs[side]:




def main():
    Robot=robot()
    Robot.BuildKineModules()
    jts=[0,10,30,0,20,0,0]
    a=Robot.GetEffectorPosition(jts)
    # print(a)
    # print('final pos')
    print(Robot.SetEffectorPosition(a)*180/m.pi)

    act=rosact()
    # act.write(Robot)
    print('this shouldnt be displayed')

if __name__== '__main__':
    main()

