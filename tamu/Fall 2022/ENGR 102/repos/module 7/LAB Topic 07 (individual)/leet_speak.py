# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   7.26.1: LAB: Leet speak
# Date:         07 October 2022

conversions = {
    "a": "4",
    "e": "3",
    "o": "0",
    "s": "5",
    "t": "7"
}

userInput = input("Enter some text: ").split()
leetString = []

for i in userInput: # replaces each letter that corresponds with a key in the dictionary to its value pair
    translate = i.maketrans(conversions)
    leetString.append(i.translate(translate))

userInputString = " ".join(userInput)
print(f"In leet speak, \"{userInputString}\" is:")
print(" ".join(leetString))
