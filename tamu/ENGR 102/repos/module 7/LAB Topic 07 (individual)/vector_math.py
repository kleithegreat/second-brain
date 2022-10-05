# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   7.27.1: LAB: Vector math
# Date:         07 October 2022

from math import sqrt

vectorA = input("Enter the elements for vector A: ").split()
vectorB = input("Enter the elements for vector B: ").split()

print(f"The magnitude of vector A is {sqrt(int(vectorA[0]) ** 2 + int(vectorA[1]) ** 2 + int(vectorA[2]) ** 2):.5f}")
print(f"The magnitude of vector B is {sqrt(int(vectorB[0]) ** 2 + int(vectorB[1]) ** 2 + int(vectorB[2]) ** 2):.5f}")
print(f"A + B is: {[float(int(x)) + float(int(vectorB[vectorA.index(x)])) for x in vectorA]}")
print(f"A - B is: {[float(int(x)) - float(int(vectorB[vectorA.index(x)])) for x in vectorA]}")
print(f"The dot product is {sum([float(int(x)) * float(int(vectorB[vectorA.index(x)])) for x in vectorA]):.2f}")
