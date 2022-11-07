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
# Assignment:   11.9.1: LAB: Passport checker Part A
# Date:         07 November 2022

validPassportsNumber = 0
validPassports = []
fileName = input("Enter the name of the file: ")

with open(fileName, "r") as scannedPassports:
    passports = scannedPassports.read().split("\n\n") # splits passports entries into a list

for i in passports:
    if "byr" in i and "iyr" in i and "eyr" in i and "hgt" in i and "ecl" in i and "pid" in i and "cid" in i:
        validPassportsNumber += 1
        validPassports.append(i)
        
with open("valid_passports.txt", "w") as validPassportsFile:
    for i in validPassports:
        validPassportsFile.write(i + "\n\n")
print(f"There are {validPassportsNumber} valid passports")
