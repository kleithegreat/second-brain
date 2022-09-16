# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kevin Lei
#               Bryan Sanchez Chavez
#               Euijin Kim
#               NAME OF TEAM MEMBER 4
# Section:      522
# Assignment:   4.14.1: LAB: Pretty equation
# Date:         16 September 2022

inputa = int(input("Please enter the coefficient A: "))
inputb = int(input("Please enter the coefficient B: "))
inputc = int(input("Please enter the coefficient C: "))

if inputa == 0:
    terma = ""
elif inputa == 1:
    terma = "x^2"
elif inputa == -1:
    terma = "- x^2"
elif inputa > 0:
    terma = f"{inputa}x^2"
else:
    terma = f"- {abs(inputa)} x^2"

if inputb == 0:
    termb = ""
elif inputb == 1:
    termb = "+ x"
elif inputb == -1:
    termb = "- x"
elif inputb > 0:
    termb = f"{inputb}x"
    if inputa != 0:
        termb = "+" + termb
else:
    termb = f"- {abs(inputb)}x"

if inputc == 0:
    termc = ""
elif inputc > 0:
    termc = f"{inputc}"
    if inputa != 0 or inputb != 0:
        termc = "+" + termc
else:
    termc = f"- {abs(inputc)}"

print("The quadratic equation is " + terma, termb, termc, "= 0")