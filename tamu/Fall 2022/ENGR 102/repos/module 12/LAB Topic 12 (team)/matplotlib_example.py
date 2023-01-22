# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kevin Lei
#               Quinn Hamilton
#               Jinyu Zhou
#               Joaquin Torres
#               
# Section:      522
# Assignment:   12.15.1: LAB: Matplotlib example
# Date:         14 November 2022

# As a team, we have gone through all required sections of the  
# tutorial, and each team member understands the material

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_ylabel("y")
ax.set_xlabel("x")
fig.suptitle("Parabola plots with varying focal length")
x = np.linspace(-2, 2, 1000)
y1 = (1 / (4 * 2)) * x**2
y2 = (1 / (4 * 6)) * x**2
ax.plot(x, y1, linewidth = 2, color = "red")
ax.plot(x, y2, linewidth = 6, color = "blue")
plt.show()



fig, ax = plt.subplots()
ax.set_ylabel("y values")
ax.set_xlabel("x values")
fig.suptitle("Plot of cubic polynomial")
x = np.linspace(-4, 4, 1000)
y = 2*x**3 + 3*x**2 - 11*x - 6
ax.plot(x, y)
plt.show()



fig, ax = plt.subplots(2)
fig.suptitle("Plot of cos(x) and sin(x)")
plt.xlabel("x")
x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y1 = np.cos(x)
ax[0].plot(x, y1, color = "red")
ax[0].set_ylabel("y=cos(x)")
y2 = np.sin(x)
ax[1].plot(x, y2, color = "grey")
ax[1].set_ylabel("y=sin(x)")
plt.show()
