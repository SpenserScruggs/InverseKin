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
    zp = z-l1
    th1 = np.arctan2(y,x)
    th3p = -np.arccos((x**2+y**2+z**2-l2**2*l3**2) / (2*l2*l3))
    r = np.sqrt(x**2+y**2+z**2)
    th2 = np.arcsin(zp/r) + np.arctan2(l3*np.sin(th3p), l2 + l3*np.cos(th3p))
    th3 = (th2 + np.pi / 2) + th3p

    return [th1, th2, th3]

# forward kinematics
def getpos(th1, th2, th3):
    global l1, l2, l3
    x = (l2*np.cos(th2) + l3*np.cos(th3))*np.cos(th1)
    y = (l2*np.cos(th2) + l3*np.cos(th3))*np.sin(th1)
    z = l1 - l2*np.sin(th2) - l3*np.sin(th3)
    return [x, y, z]

angles1 = getangles(xinput, yinput, zinput)
print(np.multiply(180 / np.pi, angles1))

print(getpos(angles1[0], angles1[1], angles1[2]))