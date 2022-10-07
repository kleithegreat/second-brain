# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   7.27.1: LAB: Vector math
# Date:         07 October 2022

from math import sqrt

vectorA = input("Enter the elements for vector A: ").split() # takes user input and parses it into an array for vectors A and B
vectorB = input("Enter the elements for vector B: ").split()

magnitudeA = 0
for i in vectorA:
    magnitudeA += float(i) ** 2
print(f"The magnitude of vector A is {sqrt(magnitudeA):.5f}")

magnitudeB = 0
for i in vectorB:
    magnitudeB += float(i) ** 2
print(f"The magnitude of vector B is {sqrt(magnitudeB):.5f}")

vectorSum = []
for i in range(len(vectorA)):
    vectorSum.append(float(vectorA[i]) + float(vectorB[i]))
print(f"A + B is {vectorSum}")

vectorDifference = []
for i in range(len(vectorA)):
    vectorDifference.append(float(vectorA[i]) - float(vectorB[i]))
print(f"A - B is {vectorDifference}")

dotProduct = 0
for i in range(len(vectorA)):
    dotProduct += float(vectorA[i]) * float(vectorB[i])
print(f"The dot product is {dotProduct:.2f}")
