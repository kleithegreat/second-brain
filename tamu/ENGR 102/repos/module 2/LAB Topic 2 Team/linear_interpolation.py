# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Daniel Mandujano
#               Valentina Gonzalez
#               Kevin Lei
#               Ximena Candelario 
# Section:      522
# Assignment:   Lab: Topic 2, Activity 3 
# Date:         09/02/2022

import math

t1 = 10 #minutes
x1 = 2026 #kilometers
t2 = 45 + t1
x2 = 23026 #kilometers

t = 25
p = (x2 - x1) / (t2 - t1) * (t - t1) + x1

print("Part 1:")
print("For t =", t, "minutes, the position p =", p, "kilometers")

t = 300
if p >= 6745:
  p = ((x2 - x1) / (t2 - t1) * (t - t1) + x1) % (math.pi * 6745 * 2)

print("Part 2:")
print("For t =", t, "minutes, the position p =", p, "kilometers")