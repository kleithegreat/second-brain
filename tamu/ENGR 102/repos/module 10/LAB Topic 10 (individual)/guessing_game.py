# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Lei
# Section:      522
# Assignment:   10.14.1: LAB: Guessing game
# Date:         31 October 2022

secret = 26

# gets the user input and checks for validity
def getInput():
    while True:
        try:
            guess = int(input())
            break
        except:
            print("Bad input! Try again:", end = " ")
            continue
    return guess

# returns 0 if the guess is correct, a negative number if guess is too low, and a positive number if guess is too high
def checkGuess(num):
    return num - secret   

print("Guess the secret number! Hint: it's an integer between 1 and 100...")
guessCount = 0
while True:
    print("What is your guess? ", end = "")
    guess = getInput()
    guessCount += 1 
    
    # prints a message based on the guess
    if checkGuess(guess) == 0:
        print(f"You guessed it! It took you {guessCount} guesses.")
        break
    elif checkGuess(guess) <= 0:
        print("Too low!")
    else:
        print("Too high!")
