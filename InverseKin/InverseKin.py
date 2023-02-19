import numpy as np
import sympy as sp
import matplotlib.pyplot as plt



l1 = 1
l2 = 1
l3 = 1

# inverse kinematics
def getangles(x, y, z):
    global l1, l2, l3

    rp = np.sqrt(x**2 + y**2 + (z - l1)**2)
    th1 = np.arctan2(y, x)
    B = np.arccos((rp**2 - l3**2 - l1**2) / (-2*l3*l2))
    th3 = np.pi - B
    th2 = np.arcsin((z-l1) / rp) + np.arctan2((l3*np.sin(th3)), (l2 + l3 * np.cos(th3)))
    
    return [th1, th2, th3]

# forward kinematics
def getpos(angles):
    global l1, l2, l3 
    
    th1 = angles[0]
    th2 = angles[1]
    th3 = angles[2]

    r = l2 * np.cos(th2) + l3 * np.cos(th2 - th3)
    x = r * np.cos(th1)
    y = r * np.sin(th1)
    z = l2 * np.sin(th2) + l3 * np.sin(th2 - th3)
    return [x, y, z]

def rad_degrees(angles):
    return [angles[0] * 180 / np.pi, angles[1] * 180 / np.pi, angles[2] * 180 / np.pi]

dimensions = 20
plt.grid(linestyle="--")
for i in range(dimensions + 1):
    for j in range(dimensions + 1):
        x = 2 * i / dimensions
        y = 0
        z = 4 * j / dimensions
        #print( "X:", x, " Y:", y, " Z:", z, "  ", rad_degrees(getangles(x, y, z)), getpos(getangles(x, y, z)))
        plt.scatter(x, z, 50, color="red", marker="*", label="input points")
        plt.scatter(getpos(getangles(x, y, z))[0], getpos(getangles(x, y, z))[2] + 1, 25, color="blue", marker="+", label="output points")

xcircle = []
ycircle = []
for i in range(100):
    xcircle.append(2 * np.cos(i / 30 - np.pi / 2))
    ycircle.append(2 * np.sin(i / 30 - np.pi / 2) + 1)

plt.plot(xcircle, ycircle)
plt.show()