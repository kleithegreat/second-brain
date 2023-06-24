# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kevin Lei
#               Bryan Sanchez Chavez
#               Euijin Kim
#               Agustin Portillo
# Section:      522
# Assignment:   4.15.1: LAB: Boolean expressions
# Date:         16 September 2022

############ Part A ############
input1 = input("Enter True or False for a: ")
input2 = input("Enter True or False for b: ")
input3 = input("Enter True or False for c: ")

a = False
if input1 == "True" or input1 == "T" or input1 == "t":
    a = True
elif input1 == "False" or input1 == "F" or input1 == "f":
    a == False

b = False
if input2 == "True" or input2 == "T" or input2 == "t":
    b = True
elif input2 == "False" or input2 == "F" or input2 == "f":
    b == False

c = False
if input3 == "True" or input3 == "T" or input3 == "t":
    c = True
elif input3 == "False" or input3 == "F" or input3 == "f":
    c == False

############ Part B ############
print(f"a and b and c: {a and b and c}")
print(f"a or b or c: {a or b or c}")

############ Part C ############
print(f"XOR: {(a and not b) or (not a and b)}")
print(f"Odd number: {(a and not b and not c) or (a and b and c) or (not a and b and not c) or (not a and not b and c)}")

############ Part D ############
print(f"Complex 1: {(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)}")
print(f"Complex 2: {(not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))}")
print(f"Simple 1: {not b or not a and not c}")
print(f"Simple 2: {not b and c or a}")
