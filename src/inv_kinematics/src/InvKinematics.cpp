#include "inv_kinematics/InvKinematics.hpp"

namespace inv_kinematics {

InvKinematics::InvKinematics(ros::NodeHandle& nodeHandle)
    : nodeHandle_(nodeHandle)
{
  if (!readOrientation()) {
    ROS_ERROR("Could not read the orientation matirx.");
    ros::requestShutdown();
  }

  joint_1_publisher = nodeHandle_.advertise<std_msgs::Float64>("/irb120/joint_1_position_controller/command", 1000);
  joint_2_publisher = nodeHandle_.advertise<std_msgs::Float64>("/irb120/joint_2_position_controller/command", 1000);
  joint_3_publisher = nodeHandle_.advertise<std_msgs::Float64>("/irb120/joint_3_position_controller/command", 1000);
  joint_4_publisher = nodeHandle_.advertise<std_msgs::Float64>("/irb120/joint_4_position_controller/command", 1000);
  joint_5_publisher = nodeHandle_.advertise<std_msgs::Float64>("/irb120/joint_5_position_controller/command", 1000);
  joint_6_publisher = nodeHandle_.advertise<std_msgs::Float64>("/irb120/joint_6_position_controller/command", 1000);
  


  tool_tip_subscriber_ = nodeHandle_.subscribe("/tool_tip_pos", 10, &InvKinematics::ikCallBack, this); 
  ROS_INFO("Successfully launched node.");

}

InvKinematics::~InvKinematics()
{
}

bool InvKinematics::readOrientation()
{
      if (!nodeHandle_.getParam("orientation_matrix", orientation_matrix_)) return false;
      return true;
}

void InvKinematics::ikCallBack(const geometry_msgs::Point& toolTipPosition)
{
    toolTipHomogeneousTransform << orientation_matrix_[0],  orientation_matrix_[1],  orientation_matrix_[2], toolTipPosition.x,
                                   orientation_matrix_[3],  orientation_matrix_[4],  orientation_matrix_[5], toolTipPosition.y,
                                  orientation_matrix_[6],  orientation_matrix_[7],  orientation_matrix_[8], toolTipPosition.z,
                                   0,  0,  0,    1;
    
    // cout << toolTipHomogeneousTransform;
    joint_angles = analytical_ik_.getJointAngles(toolTipHomogeneousTransform);
    publishJointCommands(joint_angles);
    // cout<<joint_angles;
}

void InvKinematics::publishJointCommands(const Matrix<float, 6, 1> joint_angles_)
{
    std_msgs::Float64 msg1,msg2,msg3,msg4,msg5,msg6;
   
    msg1.data = joint_angles_(0);
    msg2.data = joint_angles_(1);
    msg3.data = joint_angles_(2);
    msg4.data = joint_angles_(3);
    msg5.data = joint_angles_(4);
    msg6.data = joint_angles_(5);
    // ROS_INFO("out");
    joint_1_publisher.publish(msg1);
    joint_2_publisher.publish(msg2);
    joint_3_publisher.publish(msg3);
    joint_4_publisher.publish(msg4);
    joint_5_publisher.publish(msg5);
    joint_6_publisher.publish(msg6);
}

} /* namespace */
