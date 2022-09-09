# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   3.18 LAB: Calling functions
# Date:         9 September 2022

from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

# example function call:
# printresult(<string of shape name>, <float of side>, <float of area>)
# printresult('square', 2.236, 5)
# Your code goes here

length = float(input("Please enter the side length: "))
printresult("triangle", length, sqrt(3) / 4 * length ** 2)
printresult("square", length, length ** 2)
printresult("pentagon", length, 1/4 * sqrt(5 * (5 + 2 * sqrt(5))) * length ** 2)
printresult("dodecagon", length, 3 * (2 + sqrt(3)) * length ** 2)