# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   12.16.1: LAB: Pretty plot
# Date:         14 November 2022

import numpy as np
import matplotlib.pyplot as plt

v = np.array([0, 1])
M = np.array([[1.01, 0.09],
             [-0.09, 1.01]])
data = np.array([[0, 1]])

for i in range(200): # creates 200 additional data points
    v = np.matmul(v, M)
    data = np.concatenate((data, [v]), axis = 0)
 
fig, ax = plt.subplots()
ax.plot(data[0:200, 0], data[0:200, 1])
ax.set_ylabel("y")
ax.set_xlabel("x")
fig.suptitle("Spiral")
plt.show()
