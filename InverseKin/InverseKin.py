import numpy as np
import matplotlib.pyplot as plt

# l1 must be 1, doesnt work otherwise
l1 = 1
l2 = 1
l3 = 2

# inverse kinematics
def getangles(x, y, z):
    global l1, l2, l3

    rp = np.sqrt(x**2 + y**2 + (z - l1)**2)

    th1 = np.arctan2(y, x)
    B = np.arccos((rp**2 - l3**2 - l2**2) / (-2*l3*l2))
    #B = np.arctan2(np.sqrt(1-((rp**2 - l3**2 - l1**2) / (-2*l3*l2))**2), (rp**2 - l3**2 - l1**2) / (-2*l3*l2))
    th3 = np.pi - B
    #th3 = B
    th2 = np.arcsin((z-l1) / rp) + np.arctan2((l3*np.sin(th3)), (l2 + l3 * np.cos(th3)))
    #th2 = np.arcsin((z-l1)/rp) + np.arcsin((l3*np.sin(B)) / rp)
    #th2 = np.arctan2((z-l1)/rp, np.sqrt(1- ((z-l1)/rp)**2)) + np.arctan2((l3*np.sin(B)) / rp, np.sqrt(1 - ((l3*np.sin(B)) / rp)**2))
    
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

# converts rad to degrees
def rad_degrees(angles):
    return [angles[0] * 180 / np.pi, angles[1] * 180 / np.pi, angles[2] * 180 / np.pi]

resolution = 20
scale = 1
plt.grid(linestyle="--")
for i in range(resolution + 1):
    for j in range(resolution + 1):
        x = (-4 + 8 * i / resolution) * scale
        y = 0
        z = (-4 + 8 * j / resolution) * scale + 1
        #print( "X:", x, " Y:", y, " Z:", z, "  ", rad_degrees(getangles(x, y, z)), getpos(getangles(x, y, z)))
        plt.scatter(x, z, 50, color="red", marker="*", label="input points")
        plt.scatter(getpos(getangles(x, y, z))[0], getpos(getangles(x, y, z))[2] + 1, 25, color="blue", marker="+", label="output points")

xcircle = []
ycircle = []
for i in range(200):
    xcircle.append(2 * np.cos(i / 30))
    ycircle.append(2 * np.sin(i / 30) + 1)

plt.scatter(0, 1, 100, color="black", label="base")
plt.ylabel("z-axis")
plt.xlabel("x-axis")
plt.plot(xcircle, ycircle)
plt.xlim(-3 * scale * 1.5, 3 * scale * 1.5)
plt.ylim(-3 * scale * 1.5 + 1, 3 * scale * 1.5 + 1)
plt.show()