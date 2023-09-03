# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   6.14.1: LAB: Juggler sequence
# Date:         30 September 2022

term = int(input("Enter a positive integer: "))
count = 0
print(f"The Juggler sequence starting at {term} is:")
print(f"{term}", end = "")

# executes the algorithm until the term is equal to 1
while term != 1:
    if term % 2 == 0:
        term = int(term ** (1/2))
        print(f", {term}", end = "")
        count += 1
    else:
        term = int(term ** (3/2))
        print(f", {term}", end = "")
        count += 1

print()    
print(f"It took {count} iterations to reach 1")