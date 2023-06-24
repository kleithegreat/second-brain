# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        NAME OF TEAM MEMBER 1
#               NAME OF TEAM MEMBER 2
#               NAME OF TEAM MEMBER 3
#               NAME OF TEAM MEMBER 4
# Section:      522
# Assignment:   3.16 LAB: Still More Linear Interpolation
# Date:         9 September 2022

t1 = float(input("Enter time 1: "))
x1 = float(input("Enter the x position of the object at time 1: "))
y1 = float(input("Enter the y position of the object at time 1: "))
z1 = float(input("Enter the z position of the object at time 1: "))

t2 = float(input("Enter time 2: "))
x2 = float(input("Enter the x position of the object at time 2: "))
y2 = float(input("Enter the y position of the object at time 2: "))
z2 = float(input("Enter the z position of the object at time 2: "))

interval = (t2 - t1) / 4

for i in range (0, 5):
    print(f"At time {t1 + interval * i:.2f} seconds the object is at ({(x2 - x1) / (t2 - t1) * interval * i + x1:.3f}, {(y2 - y1) / (t2 - t1) * interval * i + y1:.3f}, {(z2 - z1) / (t2 - t1) * interval * i + z1:.3f})")