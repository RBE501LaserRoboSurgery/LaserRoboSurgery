#pragma once
#include <Eigen/Dense>
#include <iostream>

using namespace std;
using namespace Eigen;

namespace inv_kinematics {

/*!
 * Class containing the algorithmic part of the package.
 */
class AnalyticalIK
{
 public:
  /*!
   * Constructor.
   */
  AnalyticalIK();

  /*!
   * Destructor.
   */
  virtual ~AnalyticalIK();

  /*!
   * Calculate joint angles from the given tool tip position
   * @return the joint angles
   */
  Matrix<float, 6, 1> getJointAngles(MatrixXd H);

  MatrixXd getR03(Matrix<float, 3, 1> theta_);

  /*!
   * Calculate the tranformation for 1 link
   * @return the 4x4 Homogenous transformation matrix
   */
  MatrixXd MatrixTransformation(float theta, float d_, float a_, float alpha_);

 private:

  //! Internal variable to test if Eigen works
  Matrix2d testMatrix;

  //! DH Parameters of a 6DOF Robot
  Matrix<float, 6, 1> theta;
  Matrix<float, 6, 1> d;
  Matrix<float, 6, 1> a;
  Matrix<float, 6, 1> alpha;
};

} /* namespace */
