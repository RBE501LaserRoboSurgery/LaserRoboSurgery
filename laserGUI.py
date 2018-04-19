import numpy as np
import cv2

# mouse callback function
def registerClick(event,x,y,flags,param):
    global clicks, clicks_done
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if clicks_done == False:
            clicks = np.append(clicks, np.array([[x, y]]), axis = 0)
        # print(clicks)
        # print(clicks_done)

# Variable to store all the clicks
clicks = np.zeros((1,2), np.uint8)

# Status variable that defines if points for trajectory are finalized
clicks_done = False

# Final target points for the trajectory
target_points = []

# Define the frame to display everything
cv2.namedWindow('frame')

# Connect mouse interrupt
cv2.setMouseCallback('frame',registerClick)

# Get camera object
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        target_points = clicks[1:]
        print(target_points)
        for point in target_points:
            # print(point)
            if clicks_done == False:
                cv2.circle(frame,tuple(point),5,(255,0,0),-1)
            else:
                cv2.circle(frame,tuple(point),5,(0,255,0),-1)

        cv2.imshow('frame',frame)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break
        elif k == ord('d'):
            clicks_done = True

        # write the flipped frame
        # out.write(frame)
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()