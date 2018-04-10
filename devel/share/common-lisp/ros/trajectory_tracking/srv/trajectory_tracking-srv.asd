
(cl:in-package :asdf)

(defsystem "trajectory_tracking-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "TrajectoryPoint" :depends-on ("_package_TrajectoryPoint"))
    (:file "_package_TrajectoryPoint" :depends-on ("_package"))
  ))