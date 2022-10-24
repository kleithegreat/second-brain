# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   9.16.1: LAB: Small functions
# Date:         24 October 2022

from math import pi, sqrt

def parta(rSphere, rHole):
    return (4 / 3 * pi * rSphere ** 3) - (pi * rHole ** 2 * sqrt(rSphere ** 2 - rHole ** 2)) - 2 * ((pi * (rSphere - sqrt(rHole ** 2 - rSphere ** 2)) ** 2 / 3) * (3 * rSphere - (rSphere - sqrt(rHole ** 2 - rSphere ** 2))))

def partb(n):
    