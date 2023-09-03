# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   2.10.1: LAB: More Linear Interpolation
# Date:         29 August 2022

# initial time and position
t0 = 12
x0 = 8
y0 = 6
z0 = 7

# ending time and position
t2 = 85
x2 = -5
y2 = 30
z2 = 9

# interpolated position at given time starting at t = 30 seconds
t1 = 30.0

for i in range(5):
    x1 = (x2 - x0) / (t2 - t0) * (t1 - t0) + x0
    y1 = (y2 - y0) / (t2 - t0) * (t1 - t0) + y0
    z1 = (z2 - z0) / (t2 - t0) * (t1 - t0) + z0
    print("At time", t1, "seconds:")
    print("x" + str(i + 1), "=", x1, "m")
    print("y" + str(i + 1), "=", y1, "m")
    print("z" + str(i + 1), "=", z1, "m")
    if i == 4:
        break
    else:
        print("-----------------------")
        t1 += 7.5
