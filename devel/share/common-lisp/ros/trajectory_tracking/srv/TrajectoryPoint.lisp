; Auto-generated. Do not edit!


(cl:in-package trajectory_tracking-srv)


;//! \htmlinclude TrajectoryPoint-request.msg.html

(cl:defclass <TrajectoryPoint-request> (roslisp-msg-protocol:ros-message)
  ((t
    :reader t
    :initarg :t
    :type cl:float
    :initform 0.0))
)

(cl:defclass TrajectoryPoint-request (<TrajectoryPoint-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TrajectoryPoint-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TrajectoryPoint-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name trajectory_tracking-srv:<TrajectoryPoint-request> is deprecated: use trajectory_tracking-srv:TrajectoryPoint-request instead.")))

(cl:ensure-generic-function 't-val :lambda-list '(m))
(cl:defmethod t-val ((m <TrajectoryPoint-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader trajectory_tracking-srv:t-val is deprecated.  Use trajectory_tracking-srv:t instead.")
  (t m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TrajectoryPoint-request>) ostream)
  "Serializes a message object of type '<TrajectoryPoint-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 't))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TrajectoryPoint-request>) istream)
  "Deserializes a message object of type '<TrajectoryPoint-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 't) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TrajectoryPoint-request>)))
  "Returns string type for a service object of type '<TrajectoryPoint-request>"
  "trajectory_tracking/TrajectoryPointRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TrajectoryPoint-request)))
  "Returns string type for a service object of type 'TrajectoryPoint-request"
  "trajectory_tracking/TrajectoryPointRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TrajectoryPoint-request>)))
  "Returns md5sum for a message object of type '<TrajectoryPoint-request>"
  "cd4edd24fcfc9c8a5ef4de64d28e7e2c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TrajectoryPoint-request)))
  "Returns md5sum for a message object of type 'TrajectoryPoint-request"
  "cd4edd24fcfc9c8a5ef4de64d28e7e2c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TrajectoryPoint-request>)))
  "Returns full string definition for message of type '<TrajectoryPoint-request>"
  (cl:format cl:nil "float64 t~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TrajectoryPoint-request)))
  "Returns full string definition for message of type 'TrajectoryPoint-request"
  (cl:format cl:nil "float64 t~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TrajectoryPoint-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TrajectoryPoint-request>))
  "Converts a ROS message object to a list"
  (cl:list 'TrajectoryPoint-request
    (cl:cons ':t (t msg))
))
;//! \htmlinclude TrajectoryPoint-response.msg.html

(cl:defclass <TrajectoryPoint-response> (roslisp-msg-protocol:ros-message)
  ((position
    :reader position
    :initarg :position
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point)))
)

(cl:defclass TrajectoryPoint-response (<TrajectoryPoint-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TrajectoryPoint-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TrajectoryPoint-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name trajectory_tracking-srv:<TrajectoryPoint-response> is deprecated: use trajectory_tracking-srv:TrajectoryPoint-response instead.")))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <TrajectoryPoint-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader trajectory_tracking-srv:position-val is deprecated.  Use trajectory_tracking-srv:position instead.")
  (position m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TrajectoryPoint-response>) ostream)
  "Serializes a message object of type '<TrajectoryPoint-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'position) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TrajectoryPoint-response>) istream)
  "Deserializes a message object of type '<TrajectoryPoint-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'position) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TrajectoryPoint-response>)))
  "Returns string type for a service object of type '<TrajectoryPoint-response>"
  "trajectory_tracking/TrajectoryPointResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TrajectoryPoint-response)))
  "Returns string type for a service object of type 'TrajectoryPoint-response"
  "trajectory_tracking/TrajectoryPointResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TrajectoryPoint-response>)))
  "Returns md5sum for a message object of type '<TrajectoryPoint-response>"
  "cd4edd24fcfc9c8a5ef4de64d28e7e2c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TrajectoryPoint-response)))
  "Returns md5sum for a message object of type 'TrajectoryPoint-response"
  "cd4edd24fcfc9c8a5ef4de64d28e7e2c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TrajectoryPoint-response>)))
  "Returns full string definition for message of type '<TrajectoryPoint-response>"
  (cl:format cl:nil "geometry_msgs/Point position~%~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TrajectoryPoint-response)))
  "Returns full string definition for message of type 'TrajectoryPoint-response"
  (cl:format cl:nil "geometry_msgs/Point position~%~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TrajectoryPoint-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'position))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TrajectoryPoint-response>))
  "Converts a ROS message object to a list"
  (cl:list 'TrajectoryPoint-response
    (cl:cons ':position (position msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'TrajectoryPoint)))
  'TrajectoryPoint-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'TrajectoryPoint)))
  'TrajectoryPoint-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TrajectoryPoint)))
  "Returns string type for a service object of type '<TrajectoryPoint>"
  "trajectory_tracking/TrajectoryPoint")