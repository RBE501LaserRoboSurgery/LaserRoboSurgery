#include <ros/ros.h>
#include "inv_kinematics/InvKinematics.hpp"

int main(int argc, char** argv)
{
  ros::init(argc, argv, "inv_kinematics");
  ros::NodeHandle nodeHandle("~");

  inv_kinematics::InvKinematics invKinematics(nodeHandle);

  ros::spin();
  return 0;
}
