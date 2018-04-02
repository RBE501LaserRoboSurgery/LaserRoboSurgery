#include "inv_kinematics/AnalyticalIK.hpp"

namespace inv_kinematics {

AnalyticalIK::AnalyticalIK()
{
    d << 290, 0, 0, 302, 0, 72;
    a << 0, 270, 70, 0, 0, 0;
    alpha <<  90 * (M_PI, 180.0),
              0,
              90 * (M_PI, 180.0),
             -90 * (M_PI, 180.0),
              90 * (M_PI, 180.0),
              0;
    theta << 0, 0, 0, 0, 0, 0;
}

AnalyticalIK::~AnalyticalIK()
{
}


//Inverse Kinematics Function - Given any H(4x4) Matrix to get all the 6 Joint values
Matrix<float, 6, 1> AnalyticalIK::getJointAngles(MatrixXd H)
{
  int i, j, index;
  MatrixXd Pos(3,1);
  MatrixXd Rot(3,3);
  MatrixXd k(3,1);
  MatrixXd Pos1(3,1);
  Matrix<float, 6, 1> JointAngles;
  MatrixXd R03(3,3);
  MatrixXd R36(3,3);
  MatrixXd E_Pos(3,1);
  double x, y, z, R, alpha, beta, theta1,theta2, theta3, theta4, theta5, theta6, C2, S2, temp;
  for (i=0;i<=2;i++)
  {
    // Extract position from transformation matrix
    Pos(i,0)=H(i,3);

    // Why not just initialise K this way?
    if (i==2)
    {
      k(i,0)=1;
    }
    else
    {
      k(i,0)=0;
    }

    // Extract rotation matrix
    for (j=0;j<=2;j++)
    {
      Rot(i,j)=H(i,j);
    }
  }

  MatrixXd b(3,1);
  b(0,0) = 0;
  b(1,0) = 1;
  b(2,0) = 1;
  MatrixXd end(3,1);
  // E_Pos = Rot*b;
  // This is probably to translate the position from their end effector to the robot tooltip.
  //Pos(0,0) = Pos(0,0);
  //Pos(1,0) = Pos(1,0)-(32.5);
  //Pos(2,0) = Pos(2,0)+(165);

  Pos1 = Pos -  (72) * Rot * k;
  x = Pos1(0,0);
  y = Pos1(1,0);
  z = Pos1(2,0);

  // Applying trigonometrix formulae to find joint angle 2?
  theta1=atan2(y,x);
  R=sqrt(x*x+y*y);
  alpha=atan2(70,302);
  // What exactly is beta?
  beta=atan2(R,z-290);
  C2=(pow(R,2)+ pow(z-290,2)+pow(270,2)-pow(302,2)-pow(70,2))/(540*sqrt(pow(R,2)+pow(z-290,2)));
  S2=sqrt(1-pow(C2,2));

  theta2=atan2(S2,C2)-beta;

  temp=atan2(z-290-270*cos(theta2), R+270*sin(theta2));
  theta3=temp-theta2-alpha;

  Matrix<float, 3, 1> t(3);
  t(0) = (float) theta1; t(1) = (float) theta2+(90*M_PI/180.0); t(2) = (float) theta3;
  R03 = getR03(t);
  R36 = R03.transpose() * Rot;
  double S5 = sqrt(pow(R36(0,2),2) + pow(R36(1,2),2));
  theta5 = atan2(S5 , R36(2,2));

  theta4 = atan2(R36(1,2)/S5,R36(0,2)/S5);

  theta6 = atan2(R36(2,1)/S5, -R36(2,0)/S5);

  JointAngles(0)=theta1;
  JointAngles(1)=theta2;
  JointAngles(2)=theta3;
  JointAngles(3)=theta4;
  JointAngles(4)=theta5;
  JointAngles(5)=theta6;

  return JointAngles;
}

//Gives R03 matrix required for Inverse Kinematics calculation
MatrixXd AnalyticalIK::getR03(Matrix<float, 3, 1> theta_)
{
  MatrixXd R03(3,3);
  MatrixXd T03;
  MatrixXd T01;
  MatrixXd T12;
  MatrixXd T23;

  T01 = MatrixTransformation(theta_(0),d(0),a(0),alpha(0));
  T12 = MatrixTransformation(theta_(1),d(1),a(1),alpha(1));
  T23 = MatrixTransformation(theta_(2),d(2),a(2),alpha(2));
  T03 = T01 * T12 * T23;
  for (int i=0;i<3;i++)
  {
    for(int j=0;j<3;j++)
    {
      R03(i,j) = T03(i,j);
    }
  }
  return R03;
}

MatrixXd AnalyticalIK::MatrixTransformation(float theta, float d_, float a_, float alpha_)
{
  MatrixXd T01(4,4);
  T01(0,0) = cos(theta);
  T01(0,1) = -sin(theta)*cos(alpha_);
  T01(0,2) = sin(theta)*sin(alpha_);
  T01(0,3) = a_ * cos(theta);
  T01(1,0) = sin(theta);
  T01(1,1) = cos(theta)*cos(alpha_);
  T01(1,2) = -cos(theta)*sin(alpha_);
  T01(1,3) = a_ * sin(theta);
  T01(2,0) = 0;
  T01(2,1) = sin(alpha_);
  T01(2,2) = cos(alpha_);
  T01(2,3) = d_;
  T01(3,0) = 0;
  T01(3,1) = 0;
  T01(3,2) = 0;
  T01(3,3) = 1;
  return T01;
}


} /* namespace */
