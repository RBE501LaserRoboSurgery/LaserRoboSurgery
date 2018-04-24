import numpy as np
import cv2
import threading
import time
import copy
from register import *
from moveItCommunicator import *

# Scaling Factors
S_X = 0.400
S_Y = 0.300
S_Z = 0.1

# Translation factors
TRANS_X = -(S_X/2)
TRANS_Y = 0.374 - (S_Y/2)
TRANS_Z = 0.30

# print(TRANS_X)


# Variable to store all the clicks
clicks = np.zeros((1,3), np.uint8)

# Variable to indicate that we are still drawing
drawing = False

# Variable for 2 different drawing modes
drawing_mode = False # (False: Double-click point add, True: scribble mode)

# Status variable that defines if points for trajectory are finalized
clicks_done = False

# Status variable that defines if points for trajectory are finalized
clicks_done_old = False

# Final target points for the trajectory
target_points = []

# Trajectory points
trajectory_points = []

width = []
height = []

# mouse callback function
def registerClick(event, x, y, flags, param):
	global clicks, drawing
	if clicks_done == False:
		if drawing_mode  == False:		# Double click mode
			if event == cv2.EVENT_LBUTTONDBLCLK:
				clicks = np.append(clicks, np.array([[x, y, 0]]), axis = 0)

		else:					# Scribble mode
			if event == cv2.EVENT_LBUTTONDOWN:
				drawing = True

			elif event == cv2.EVENT_MOUSEMOVE:
				if drawing == True:
					clicks = np.append(clicks, np.array([[x, y, 0]]), axis = 0)

			elif event == cv2.EVENT_LBUTTONUP:
				drawing = False
				clicks = np.append(clicks, np.array([[x, y, 0]]), axis = 0)
	# print(clicks)
	# print(clicks_done)
	

def scalePoints(points, sx, sy, sz):
	scale = np.array([sx, sy, sz])
	return np.multiply(points, scale)

def translatePoints(points, tx, ty, tz):
	trans = np.array([tx, ty, tz])
	return np.add(points, trans)

def flipYAxis(points, ymax):
	flipped_y = np.copy(points)
	flipped_y[:, 1] = ymax - flipped_y[:, 1]
	return flipped_y

def convertToFloat(points):
	return np.asfarray(points)

def convertCamToWorld(points):
	# Make a copy of the points
	cam_points = np.copy(points)

	# # Get frame size
	# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
	# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

	printPoints(cam_points, 'Cam-Points')

	# Transform cam to world 
	# printPoints(translatePoints(scalePoints(flipYAxis(cam_points, height), S_X/width, S_Y/height, S_Z), TRANS_X, TRANS_Y, TRANS_Z), 'Flipped>Scaled>Trans')
	world_points = translatePoints(scalePoints(flipYAxis(cam_points, height), S_X/width, S_Y/height, S_Z), TRANS_X, TRANS_Y, TRANS_Z)

	printPoints(world_points, 'World-Points')

	return world_points

def printPoints(points, point_name):
	print('{0}\n {1}: \n{2}\n'.format(time.ctime(time.time()), point_name, points))


def renderGUI(thread_name, delay):
	# count = 0
	# while count < 5:
	# 	time.sleep(delay)
	# 	count += 1
	# 	# print "%s: %s" % (threadName, time.ctime(time.time()))
	# 	print('{0} and {1}'.format(thread_name, time.ctime(time.time())))
	global clicks, clicks_done, target_points, cap, drawing_mode, width, height


	reg_pts = getRegistration()
	print(reg_pts)
	
	# Get camera object
	cap = cv2.VideoCapture(1)

	# Reduce the size of video to 320x240 so rpi can process faster
	cap.set(3,640)
	cap.set(4,480)

	# Get frame size
	width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
	height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

	pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
	print(pts2)
	M = cv2.getPerspectiveTransform(reg_pts.astype(np.float32), pts2)

	# cv2.namedWindow('test')



	# Define the frame to display everything
	cv2.namedWindow('frame')

	# Connect mouse interrupt
	cv2.setMouseCallback('frame',registerClick)


	# Define the codec and create VideoWriter object
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter('output.avi',fourcc, 30.0, (640,480))

	
	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret == True:

			# Transform the image according to registration points
			frame = cv2.warpPerspective(frame, M, (int(width), int(height)))			

			# Draw crosshair at frame center
			cv2.drawMarker(frame, (int(width/2), int(height/2)), (0,0,255))


			# Draw clicked points
			target_points = clicks[1:]
			# print(target_points)
			for point in target_points:
				# print(point)
				if clicks_done == False:
					cv2.circle(frame, (point[0], point[1]), 5, (255,0,0), -1)
				else:
					cv2.circle(frame, (point[0], point[1]), 5, (0,255,0), -1)			


			# # If the trajectory points are available, draw them
			# for point in trajectory_points:
			# 	# print(point)
			# 	if clicks_done == False:
			# 		cv2.circle(frame, (point[0], point[1]), 5, (255,0,0), -1)
			# 	else:
			# 		cv2.circle(frame, (point[0], point[1]), 5, (0,255,0), -1)


			cv2.imshow('frame', frame)


			# cv2.imshow('test', dst)

			k = cv2.waitKey(1) & 0xFF
			if k == ord('q'):		# Quit
				break
			elif k == ord('d'):		# Points selection done
				clicks_done = True
			elif k == ord('c'):		# Clear points
				clicks = np.zeros((1,3), np.uint8)
				target_points = []
				clicks_done = False
			elif k == ord('m'):		# Toggle drawing mode
				drawing_mode = not drawing_mode
				if drawing_mode == False:
					print('Double-click draw mode selected')
				else:
					print('Scribble draw mode selected')


			# write the flipped frame
			out.write(frame)
		else:
			break

	# Release everything if job is finished
	cap.release()
	out.release()
	cv2.destroyAllWindows()

def printInfo(delay):
	global clicks_done_old

	# # Initialize communication with moveIt
	initCommunicator()
	time.sleep(5)

	# # Go to home
	# goHome()
	# time.sleep(2)

	# # Go to home
	goLaserHome()


	while 1:
		# time.sleep(delay)

		# TEST CALLS
		# print "%s: %s" % (threadName, time.ctime(time.time()))
		# print('{0} Clicks_done: {1} and Click_points: {2}'.format(time.ctime(time.time()), clicks_done, target_points))

		# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
		# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

		# print('{0}\n Points: \n{1}\n'.format(time.ctime(time.time()), target_points))
		# print('{0}\n Points Normalized: \n{1}\n'.format(time.ctime(time.time()), scalePoints(target_points, 1/width, 1/height, 1)))
		# print('{0}\n Points translated: \n{1}\n'.format(time.ctime(time.time()), translatePoints(target_points, 10, 20, 30)))
		# print('{0}\n Y_flipped: \n{1}\n'.format(time.ctime(time.time()), flipYAxis(target_points, height)))

		# If we just transition to clicks done
		if clicks_done_old == False and clicks_done == True:

			# Convert point from cam frame to world frame
			world_pts = convertCamToWorld(target_points)

			# Forward points to moveIt interface
			goToWaypoints(world_pts)

			# Go back to laser home
			goLaserHome()

		# If we just cleared the previous trajectory
		elif clicks_done_old == True and clicks_done == False:

			# Go back to laser home
			goLaserHome()

			# Stop the old execution
			print('Stop execution')

		# Update old state
		clicks_done_old = copy.deepcopy(clicks_done)



# Create two threads as follows
t1 = threading.Thread(target = renderGUI, args = ("Thread-1", 1,))
# t2 = threading.Thread(target = printInfo, args = (1,))


t1.start()
# t2.start()

printInfo(1,)

t1.join()
# t2.join()


# pts1 = getRegistration()
# pts2 = pts2 = np.float32([[0, 0], [640, 0], [640, 480], [0, 480]])
# M = cv2.getPerspectiveTransform(pts1.astype(np.float32), pts2)
# print(M)