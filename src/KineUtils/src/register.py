import numpy as np
import cv2

# Variable to store all the registration points
registrationPts = np.zeros((1,2), np.float32)

num_regis = 0

registration_done = False

# mouse callback function
def mouseEvent(event, x, y, flags, param):
	global registrationPts, num_regis, registration_done
	if registration_done == False:
		if event == cv2.EVENT_LBUTTONDBLCLK:
			registrationPts = np.append(registrationPts, np.array([[x, y]]), axis = 0)
			num_regis = num_regis + 1
			if num_regis >= 4:
				registration_done = True


def getRegistration():

	# Get camera object
	cap = cv2.VideoCapture(1)

	# Reduce the size of video to 320x240 so rpi can process faster
	cap.set(3,640)
	cap.set(4,480)

		# Define the frame to display everything
	cv2.namedWindow('frame')

	# Connect mouse interrupt
	cv2.setMouseCallback('frame',mouseEvent)


	# Define the codec and create VideoWriter object
	# fourcc = cv2.VideoWriter_fourcc(*'XVID')
	# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

	
	while(cap.isOpened() and registration_done == False):
		ret, frame = cap.read()
		if ret == True:

			# Get frame size
			width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
			height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

			# Draw crosshair at frame center
			cv2.drawMarker(frame, (int(width/2), int(height/2)), (0,0,255))


			# Draw clicked points
			target_points = registrationPts[1:]
			# print(target_points)
			for point in target_points:
				# print(point)
				cv2.circle(frame, (int(point[0]), int(point[1])), 5, (255,0,0), -1)


			# # If the trajectory points are available, draw them
			# for point in trajectory_points:
			# 	# print(point)
			# 	if clicks_done == False:
			# 		cv2.circle(frame, (point[0], point[1]), 5, (255,0,0), -1)
			# 	else:
			# 		cv2.circle(frame, (point[0], point[1]), 5, (0,255,0), -1)


			cv2.imshow('frame',frame)
			k = cv2.waitKey(1) & 0xFF
			if k == ord('q'):		# Quit
				break

		else:
			break

	# Release everything if job is finished
	cap.release()
	# out.release()
	cv2.destroyAllWindows()

	target_points = registrationPts[1:]
	return target_points