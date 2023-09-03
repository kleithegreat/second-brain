# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   2.9.1: LAB: Using Variables
# Date:         29 August 2022

from math import *
from pydoc import tempfilepager

# newtons second law
mass = 3 # kilograms
acceleration = 5.5 # kg m/s^2
print("Force is", mass * acceleration, "N")

# bragg's law
wavelength = 0.025 # nanometers
scattering_angle = 25 # degrees
diffraction_order = 1 # orders of diffraction
print("Wavelength is", (2 * wavelength * sin(scattering_angle * pi/180)) / diffraction_order, "nm") # 2 is a constant in the equation, pi/180 converts from degrees to radians for evaluation

# radioactive decay
initial_mass = 5 # grams
t = 3 # time of decay in days
half_life = 3.8 # half life of isotope in days
print("Radon-222 left is", initial_mass * 2 ** (-t/half_life), "g") # 2 is a constant in the equation

# ideal gas law
amount = 5 # moles
CONST_R = 8.314 # m^3Pa/K * mol
temperature = 415 # kelvin
volume = 0.25 # m^3
print("Pressure is", (amount * CONST_R * temperature) / volume / 1000 , "kPa") # divide by 1000 to convert from pascals to kPa