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
# Assignment:   11.10.1: LAB: Passport checker Part B
# Date:         07 November 2022

fileName = input("Enter the name of the file: ")
with open(fileName, "r") as scannedPassports:
    passports = scannedPassports.read().split("\n\n") # splits passports entries into a list

firstFilter = []
for i in passports:
    if "byr" in i and "iyr" in i and "eyr" in i and "hgt" in i and "ecl" in i and "pid" in i and "cid" in i:
        firstFilter.append(i)

validPassportsCount = 0
validPassports = []
for i in firstFilter:
    byr = int(i[i.index("byr") + 4:i.index("byr") + 8])
    if byr < 1920 or byr > 2005:
        continue
    iyr = int(i[i.index("iyr") + 4:i.index("iyr") + 8])
    if iyr < 2012 or iyr > 2022:
        continue
    eyr = int(i[i.index("eyr") + 4:i.index("eyr") + 8])
    if eyr < 2022 or eyr > 2032:
        continue
    if "cm" in i[i.index("hgt") + 4:i.index("hgt") + 9]:
        try:
            hgt = int(i[i.index("hgt") + 4:i.index("hgt") + 7])
        except:
            continue
        if hgt < 150 or hgt > 193:
            continue
    else:
        hgt = int(i[i.index("hgt") + 4:i.index("hgt") + 6])
        if hgt < 59 or hgt > 76:
            continue
    ecl = i[i.index("ecl") + 4:i.index("ecl") + 7]
    if ecl not in "amb blu brn gry grn hzl oth":
        continue
    try:
        pid = int(i[i.index("pid") + 4:i.index("pid") + 9])
    except ValueError:
        continue
    cid = int(i[i.index("cid") + 4:i.index("cid") + 7])
    if cid < 100:
        continue
    validPassportsCount += 1
    validPassports.append(i)

with open("valid_passports2.txt", "w") as validPassportsFile:
    for i in validPassports:
        validPassportsFile.write(i + "\n\n")
print(f"There are {validPassportsCount} valid passports")
