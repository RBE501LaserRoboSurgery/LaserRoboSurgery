import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.interpolate

#for line
def draw_line(x1,y1,x2,y2):
    #slope
    m = ((y2 - y1)/(x2 - x1))
    points =[]
    line =[]
    for x in np.arange(0,10,0.5):
        y = (x-x1)*m + y1
        points.append([x,y])
        line.append(y)

    plt.plot(line)
    plt.show()
    print("Line points are:", points)
Line = draw_line(0,0,10,20)

# For arc
coords = np.array([[0, 0], [25, 10], [50, 50]])

#The curve fits as a quadratic equation on three points
f = scipy.interpolate.interp1d(coords[:, 0], coords[:, 1], kind='quadratic')

#New points will be evenly distributed along x
new_x = np.linspace(np.min(coords[:, 0]), np.max(coords[:, 0]), 20)
new_y = f(new_x)

new_coords = np.vstack([new_x, new_y]).T
plt.plot(new_y)
plt.show()
print("Arc points are:", new_coords)
