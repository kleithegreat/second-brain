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
# Assignment:   12.14.1: LAB: Numpy example
# Date:         14 November 2022

# As a team, we have gone through all required sections of the  
# tutorial, and each team member understands the material

import numpy as np

A = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])

B = np.array([[0, 1],
              [2, 3],
              [4, 5],
              [6, 7]])

C = np.array([[0, 1, 2],
              [3, 4, 5]])

D = np.matmul(np.matmul(A, B), C)

E = np.sqrt(D) / 2

print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")
print(f"D = {D}")
print(f"D^T = {D.transpose()}")
print(f"E = {E}")
