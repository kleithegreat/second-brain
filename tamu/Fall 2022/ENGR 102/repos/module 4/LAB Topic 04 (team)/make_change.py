# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kevin Lei
#               Bryan Sanchez Chavez
#               Euijin Kim
#               Agustin Portillo
# Section:      522
# Assignment:   4.13 LAB: Make change
# Date:         16 September 2022

pay = float(input("How much did you pay?"))
cost = float(input("How much did it cost?"))
change = round((pay - cost), 2)

print(f"You received ${change:.2f} in change. That is...")

# goes through each change denomination and finds amount
if change >= 0.25:
  quarters = change // 0.25
  change -= quarters * 0.25
  change = round(change, 2)
  print(f"{int(quarters)} quarters" if quarters > 1 else "1 quarter")
if change >= 0.1:
  dimes = change // 0.1
  change -= round((dimes * 0.1), 2)
  change = round(change, 2)
  print(f"{int(dimes)} dimes" if dimes > 1 else "1 dime")
if change >= 0.05:
  nickels = change // 0.05
  change -= round((nickels * 0.05), 2)
  change = round(change, 2)
  print(f"{int(nickels)} nickels" if nickels > 1 else "1 nickel")
if change >= 0.01:
    pennies = change / 0.01
    print(f"{int(pennies)} pennies" if pennies > 1 else "1 penny")