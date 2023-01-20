# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   11.11.1: LAB: Barcode checker
# Date:         07 November 2022

validBarcodes = [] # STRINGS
numValid = 0
with open(input("Enter the name of the file: "), "r") as barcodesFile:
    barcodes = barcodesFile.read().split("\n")
    
for i in barcodes:
    if 10 - int(str(3 * sum([int(j) for j in i[1: 12: 2]]) + sum([int(j) for j in i[0: 12: 2]]))[-1]) == int(i[-1]):
        numValid += 1
        validBarcodes.append(i)
validBarcodes[:-1] = [i + "\n" for i in validBarcodes[:-1]]

with open("valid_barcodes.txt", "w") as validBarcodesFile:
    for i in validBarcodes:
        validBarcodesFile.write(i)
print(f"There are {numValid} valid barcodes")
