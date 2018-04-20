import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.interpolate


#for line
def draw_line(x1,y1,x2,y2):

    if x2 > x1 or x1 > x2:
        points =[]
        line =[]
        X =[]
        m = ((y2 - y1)/(x2 - x1))
        i = (x2-x1)/10
        for x in np.arange(x1,x2,i):
            y = (x-x1)*m + y1
            points.append([x,y])
            line.append(y)
            X.append(x)
        points = np.array(points)
        plt.plot(X,line)
        plt.show()
        print("Line points are:", points)

    elif x1 == x2:
        points =[]
        line =[]
        X =[]
        m = 0
        i = ((y2 -y1)/10)
        for y in np.arange(y1,y2,i):
            x = x1
            y2 = (x-x1)*m + y
            points.append([x,y])
            line.append(y)
            X.append(x)
        points = np.array(points)
        plt.plot(X,line)
        plt.show()
        print("Line points are:", points)

# For arc
def draw_arc(x1,y1,x2,y2,x3,y3):
    coords = np.array([[x1,y1], [x2, y2], [x3, y3]])

    #The curve fits as a quadratic equation on three points
    f = scipy.interpolate.interp1d(coords[:, 0], coords[:, 1], kind='quadratic')

    #New points will be evenly distributed along x
    new_x = np.linspace(np.min(coords[:, 0]), np.max(coords[:, 0]), 20)
    new_y = f(new_x)

    new_coords = np.vstack([new_x, new_y]).T
    plt.plot(new_x, new_y)
    plt.show()
    print("Arc points are:", new_coords)

#draw Spline
def draw_spline(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5):
    coords = np.array([[x1,y1], [x2, y2], [x3, y3], [x4,y4], [x5,y5]])

    #The curve fits as a quadratic equation on five points
    f = scipy.interpolate.interp1d(coords[:, 0], coords[:, 1], kind='quadratic')

    #New points will be evenly distributed along x
    new_x = np.linspace(np.min(coords[:, 0]), np.max(coords[:, 0]), 20)
    new_y = f(new_x)

    new_coords = np.vstack([new_x, new_y]).T
    plt.plot(new_x,new_y)
    plt.show()
    print("Spline points are:", new_coords)

print("Choose a trajectory")
a =input("Press 1 for line \nPress 2 for arc  \nPress 3 for spline \n")

if a == '1':
    print("Enter 2 points for the line")
    x1 = int(input("enter x1: "))
    y1 = int(input("enter y1: "))
    x2 = int(input("enter x2: "))
    y2 = int(input("enter y2: "))
    Line = draw_line(x1,y1,x2,y2)
    #print("HI")
elif a== '2':
    print("Enter 3 points for the arc")
    x1 = int(input("enter x1: "))
    y1 = int(input("enter y1: "))
    x2 = int(input("enter x2: "))
    y2 = int(input("enter y2: "))
    x3 = int(input("enter x3: "))
    y3 = int(input("enter y3: "))
    Arc = draw_arc(x1,y1,x2,y2,x3,y3)
elif a == '3':
    print("Enter 5 points for the spline")
    x1 = int(input("enter x1: "))
    y1 = int(input("enter y1: "))
    x2 = int(input("enter x2: "))
    y2 = int(input("enter y2: "))
    x3 = int(input("enter x3: "))
    y3 = int(input("enter y3: "))
    x4 = int(input("enter x4: "))
    y4 = int(input("enter y4: "))
    x5 = int(input("enter x5: "))
    y5 = int(input("enter y5: "))
    Spline = draw_spline(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5)
else:
    print("Enter a valid number!")
