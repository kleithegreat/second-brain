# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   3.17.1: LAB: Using input
# Date:         9 September 2022

from math import *

# newtons second law
print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg): "))
acceleration = float(input("Please enter the acceleration (m/s^2): "))
print(f"Force is {mass * acceleration:.1f} N")

# bragg's law
print("This program calculates the wavelength given distance and angle")
wavelength = float(input("Please enter the distance (nm): "))
scattering_angle = float(input("Please enter the angle (degrees): "))
diffraction_order = 1
print(f"Wavelength is {(2 * wavelength * sin(scattering_angle * pi/180)) / diffraction_order:.4f} nm")

# radioactive decay
print("This program calculates how much Radon-222 is left given time and initial amount")
t = float(input("Please enter the time (days): "))
initial_mass = float(input("Please enter the initial amount (g): "))
half_life = 3.8 # half life of isotope in days
print(f"Radon-222 left is {initial_mass * 2 ** (-t/half_life):.2f} g")

# ideal gas law
print("This program calculates the pressure given moles, volume, and temperature")
amount = float(input("Please enter the number of moles: "))
volume = float(input("Please enter the volume (m^3): "))
temperature = float(input("Please enter the temperature (K): "))
CONST_R = 8.314 # m^3Pa/K * mol
print(f"Pressure is {(amount * CONST_R * temperature) / volume / 1000:.0f} kPa") # divide by 1000 to convert from pascals to kPa