# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   3.19 LAB: Challenge program
# Date:         9 September 2022

import math

precision = int(input("Please enter the number of digits of precision for e: "))
print(f"The value of e to {precision} digits is: {math.e:.{precision}f}")