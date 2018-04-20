import numpy as np
import cv2
import threading
import time

# Variable to store all the clicks
clicks = np.zeros((1,2), np.uint8)

# Status variable that defines if points for trajectory are finalized
clicks_done = False

# Final target points for the trajectory
target_points = []


# mouse callback function
def registerClick(event,x,y,flags,param):
	global clicks, clicks_done
	if event == cv2.EVENT_LBUTTONDBLCLK:
		if clicks_done == False:
			clicks = np.append(clicks, np.array([[x, y]]), axis = 0)
		# print(clicks)
		# print(clicks_done)


def renderGUI(thread_name, delay):
	# count = 0
	# while count < 5:
	# 	time.sleep(delay)
	# 	count += 1
	# 	# print "%s: %s" % (threadName, time.ctime(time.time()))
	# 	print('{0} and {1}'.format(thread_name, time.ctime(time.time())))


	# Define the frame to display everything
	cv2.namedWindow('frame')

	# Connect mouse interrupt
	cv2.setMouseCallback('frame',registerClick)

	# Get camera object
	cap = cv2.VideoCapture(0)

	# Define the codec and create VideoWriter object
	# fourcc = cv2.VideoWriter_fourcc(*'XVID')
	# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

	
	global clicks, clicks_done, target_points
	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret == True:

			target_points = clicks[1:]
			# print(target_points)
			for point in target_points:
				# print(point)
				if clicks_done == False:
					cv2.circle(frame,tuple(point),5,(255,0,0),-1)
				else:
					cv2.circle(frame,tuple(point),5,(0,255,0),-1)

			cv2.imshow('frame',frame)
			k = cv2.waitKey(1) & 0xFF
			if k == ord('q'):		# Quit
				break
			elif k == ord('d'):		# Points selection done
				clicks_done = True
			elif k == ord('c'):		# Clear points
				clicks = np.zeros((1,2), np.uint8)
				target_points = []
				clicks_done = False

			# write the flipped frame
			# out.write(frame)
		else:
			break

	# Release everything if job is finished
	cap.release()
	# out.release()
	cv2.destroyAllWindows()

def printInfo(delay):
	global clicks, clicks_done
	while 1:
		time.sleep(delay)
		# print "%s: %s" % (threadName, time.ctime(time.time()))
		print('{0} Clicks_done: {1} and Click_points: {2}'.format(time.ctime(time.time()), clicks_done, target_points))


# Create two threads as follows
t1 = threading.Thread(target = renderGUI, args = ("Thread-1", 1,))
t2 = threading.Thread(target = printInfo, args = (1,))

t1.start()
t2.start()

t1.join()
t2.join()
