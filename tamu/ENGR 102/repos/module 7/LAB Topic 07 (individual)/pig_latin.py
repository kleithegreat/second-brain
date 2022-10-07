# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   7.25.1: LAB: Pig latin
# Date:         07 October 2022

userInput = input("Enter word(s) to convert to Pig Latin: ").split()
pigLatin = []
for i in userInput: # rearranges the letters based on the pig latin rules
    if i[0].lower() in ["a", "e", "i", "o", "u", "y"]:
        pigLatin.append(i + "yay")
    else:
        j = 0
        while not i[j + 1] in ["a", "e", "i", "o", "u", "y"]:
            j += 1
        pigLatin.append(i[j + 1:len(i)] + i[0:j + 1] + "ay")

inputString = " ".join(userInput)
pigLatinString = " ".join(pigLatin)
print(f"In Pig Latin, \"{inputString}\" is: {pigLatinString}")
