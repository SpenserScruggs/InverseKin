import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


l1 = 1
l2 = 1
l3 = 1

xinput = float(input("X: "))
yinput = float(input("Y: "))
zinput = float(input("Z: "))


# Potential inverse kinematics https://www.ijcaonline.org/archives/volume179/number37/farman-2018-ijca-916848.pdf

# inverse kinematics
def getangles(x, y, z):
    global l1, l2, l3
    rp = np.sqrt(x**2 + y**2 + (z - l1)**2)
    th1 = np.arctan2(y, x)
    th3 = np.pi - np.arccos((rp**2 - l3**2 - l1**2) / (-2*l3*l2))
    th2 = np.arctan2(z - l1, np.sqrt(x**2 + y**2)) + np.arcsin((l3 * np.sin(np.pi - th3)) / np.sqrt(x**2 + y**2 + (z - l1)**2))
    #th3 = th2 + np.pi/2 - th3
    return [th1, th2, th3]

# forward kinematics
def getpos(th1, th2, th3):
    global l1, l2, l3
    x = (l2*np.cos(th2) + l3*np.cos(th2 + th3))*np.cos(th1)
    y = (l2*np.cos(th2) + l3*np.cos(th2 + th3))*np.sin(th1)
    z = l1 - l2*np.sin(th2) - l3*np.sin(th2 + th3)
    return [x, y, z]

angles1 = getangles(xinput, yinput, zinput)
print(np.multiply(180 / np.pi, angles1))

print(getpos(angles1[0], angles1[1], angles1[2]))