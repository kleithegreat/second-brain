# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kevin Lei
#               Bryan Sanchez Chavez
#               Euijin Kim
#               Agustin Portillo
# Section:      522
# Assignment:   6.11.1: LAB: Pyramid area (part 1)
# Date:         30 September 2022

from math import sqrt

length = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))
area = 0

for i in range(1, layers + 1):
    area += 3 * i * length ** 2 + ((sqrt(3) / 4) * length ** 2) * i ** 2 - ((sqrt(3) / 4) * length ** 2) * (i - 1) ** 2

print(f"You need {area:.2f} m^2 of gold foil to cover the pyramid")
