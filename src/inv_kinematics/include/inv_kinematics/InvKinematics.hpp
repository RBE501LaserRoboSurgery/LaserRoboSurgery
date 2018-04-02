#pragma once

#include "inv_kinematics/AnalyticalIK.hpp"

// ROS
#include <ros/ros.h>
#include <std_msgs/Float64.h>
#include <geometry_msgs/Point.h>

namespace inv_kinematics {

/*!
 * Main class which handled ROS interfacing of the IK solution
 */
class InvKinematics
{
 public:
  /*!
   * Constructor.
   * @param nodeHandle the ROS node handle.
   */
  InvKinematics(ros::NodeHandle& nodeHandle);

  /*!
   * Destructor.
   */
  virtual ~InvKinematics();

 private:
  /*!
   * Reads and verifies the tool tip orientation
   * @return true if successful.
   */
   bool readOrientation();

  /*!
   * Callback method for the end effector position subscriber
   * @param toolTipPosition Position of the tooltip
   */

  void ikCallBack(const geometry_msgs::Point& toolTipPosition);

  /*!
   * Function which publishes the joint commands to respective topics
   * @param joint_angles_ the joint angle value that need to be published
   */
  void publishJointCommands(const Matrix<float, 6, 1> joint_angles_);

  //! ROS node handle.
  ros::NodeHandle& nodeHandle_;

  //! Subscriber of the tool tip position
  ros::Subscriber tool_tip_subscriber_;

  //! Stores the orientation of the end effector from ROS Parameters
  vector<float> orientation_matrix_;
  
  //! Joint Command publishers
  ros::Publisher joint_1_publisher;
  ros::Publisher joint_2_publisher;
  ros::Publisher joint_3_publisher;
  ros::Publisher joint_4_publisher;
  ros::Publisher joint_5_publisher;
  ros::Publisher joint_6_publisher;

  //! Algorithm computation object.
  AnalyticalIK analytical_ik_;

  //! Vector Declarations
  Matrix<float, 6, 1> joint_angles;
  Matrix4d toolTipHomogeneousTransform;
};

} /* namespace */
