# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kevin Lei
#               Bryan Sanchez Chavez
#               Euijin Kim
#               Agustin Portillo
# Section:      522
# Assignment:   6.12.1: LAB: Pyramid area (part 2)
# Date:         30 September 2022

from math import sqrt

length = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))
# calculated by the side area plus the top area minus the last top area for each layer using an arithmetic series
area = (3 * length ** 2 * (layers * (layers + 1) / 2)) + ((sqrt(3) / 4) * length ** 2 * (layers * (layers + 1) * (2 * layers + 1) / 6)) - ((sqrt(3) / 4) * length ** 2 * (layers * (layers - 1) * (2 * (layers - 1) + 1) / 6))

print(f"You need {area:.2f} m^2 of gold foil to cover the pyramid")
