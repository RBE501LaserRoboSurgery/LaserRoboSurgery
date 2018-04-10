;; Auto-generated. Do not edit!


(when (boundp 'trajectory_tracking::TrajectoryPoint)
  (if (not (find-package "TRAJECTORY_TRACKING"))
    (make-package "TRAJECTORY_TRACKING"))
  (shadow 'TrajectoryPoint (find-package "TRAJECTORY_TRACKING")))
(unless (find-package "TRAJECTORY_TRACKING::TRAJECTORYPOINT")
  (make-package "TRAJECTORY_TRACKING::TRAJECTORYPOINT"))
(unless (find-package "TRAJECTORY_TRACKING::TRAJECTORYPOINTREQUEST")
  (make-package "TRAJECTORY_TRACKING::TRAJECTORYPOINTREQUEST"))
(unless (find-package "TRAJECTORY_TRACKING::TRAJECTORYPOINTRESPONSE")
  (make-package "TRAJECTORY_TRACKING::TRAJECTORYPOINTRESPONSE"))

(in-package "ROS")



(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass trajectory_tracking::TrajectoryPointRequest
  :super ros::object
  :slots (_t ))

(defmethod trajectory_tracking::TrajectoryPointRequest
  (:init
   (&key
    ((:t __t) 0.0)
    )
   (send-super :init)
   (setq _t (float __t))
   self)
  (:t
   (&optional __t)
   (if __t (setq _t __t)) _t)
  (:serialization-length
   ()
   (+
    ;; float64 _t
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _t
       (sys::poke _t (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _t
     (setq _t (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass trajectory_tracking::TrajectoryPointResponse
  :super ros::object
  :slots (_position ))

(defmethod trajectory_tracking::TrajectoryPointResponse
  (:init
   (&key
    ((:position __position) (instance geometry_msgs::Point :init))
    )
   (send-super :init)
   (setq _position __position)
   self)
  (:position
   (&rest __position)
   (if (keywordp (car __position))
       (send* _position __position)
     (progn
       (if __position (setq _position (car __position)))
       _position)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Point _position
    (send _position :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Point _position
       (send _position :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Point _position
     (send _position :deserialize buf ptr-) (incf ptr- (send _position :serialization-length))
   ;;
   self)
  )

(defclass trajectory_tracking::TrajectoryPoint
  :super ros::object
  :slots ())

(setf (get trajectory_tracking::TrajectoryPoint :md5sum-) "cd4edd24fcfc9c8a5ef4de64d28e7e2c")
(setf (get trajectory_tracking::TrajectoryPoint :datatype-) "trajectory_tracking/TrajectoryPoint")
(setf (get trajectory_tracking::TrajectoryPoint :request) trajectory_tracking::TrajectoryPointRequest)
(setf (get trajectory_tracking::TrajectoryPoint :response) trajectory_tracking::TrajectoryPointResponse)

(defmethod trajectory_tracking::TrajectoryPointRequest
  (:response () (instance trajectory_tracking::TrajectoryPointResponse :init)))

(setf (get trajectory_tracking::TrajectoryPointRequest :md5sum-) "cd4edd24fcfc9c8a5ef4de64d28e7e2c")
(setf (get trajectory_tracking::TrajectoryPointRequest :datatype-) "trajectory_tracking/TrajectoryPointRequest")
(setf (get trajectory_tracking::TrajectoryPointRequest :definition-)
      "float64 t
---
geometry_msgs/Point position


================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
")

(setf (get trajectory_tracking::TrajectoryPointResponse :md5sum-) "cd4edd24fcfc9c8a5ef4de64d28e7e2c")
(setf (get trajectory_tracking::TrajectoryPointResponse :datatype-) "trajectory_tracking/TrajectoryPointResponse")
(setf (get trajectory_tracking::TrajectoryPointResponse :definition-)
      "float64 t
---
geometry_msgs/Point position


================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
")



(provide :trajectory_tracking/TrajectoryPoint "cd4edd24fcfc9c8a5ef4de64d28e7e2c")


