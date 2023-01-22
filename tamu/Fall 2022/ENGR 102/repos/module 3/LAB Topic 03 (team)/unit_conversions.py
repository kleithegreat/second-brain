# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kevin Lei
#               NAME OF TEAM MEMBER 2
#               NAME OF TEAM MEMBER 3
#               NAME OF TEAM MEMBER 4
# Section:      522
# Assignment:   3.15 LAB: Unit Conversions
# Date:         9 September 2022

quantity = float(input("Please enter the quantity to be converted: "))

print(f"{quantity:.2f} pounds force is equivalent to {quantity * (3858.97/867.53):.2f} Newtons")
print(f"{quantity:.2f} meters is equivalent to {quantity * 3.28083991:.2f} feet")
print(f"{quantity:.2f} atmospheres is equivalent to {quantity * 101.325:.2f} kilopascals")
print(f"{quantity:.2f} watts is equivalent to {quantity * 3.412142:.2f} BTU per hour")
print(f"{quantity:.2f} liters per second is equivalent to {quantity * (13750.65/867.5309):.2f} US gallons per minute")
print(f"{quantity:.2f} degrees Celsius is equivalent to {quantity * 9 / 5 + 32:.2f} degrees Fahrenheit")