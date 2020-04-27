#Guess The Number

import random

print("No of games that you would like to play")
noOfGames=int(input())

randomNumber=random.randrange(1,25)

guess=0
while guess<noOfGames:
    print("Select a no between 1 and 25")
    numberSelect=int(input())

    guess=guess+1

    if numberSelect<randomNumber:
        print("Guessed number is too low")
    if numberSelect>randomNumber:
        print("Guessed Nu,ber is too high")
    if numberSelect==randomNumber:
        break

if numberSelect==randomNumber:
    guess=str(guess)
    print("Great ! you guessed my number in "+guess)

if numberSelect!=randomNumber:
    print("Nope! The guessed number is "+str(randomNumber))
"""
# This is a guess the number game.

import random

guessesTaken = 0

print('Hello! What is your name?')

myName = input()

number = random.randint(1, 20)

print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

print("No of games")
noOfGames=int(input())

while guessesTaken < noOfGames:

    print('Take a guess.') # There are four spaces in front of print.

    guess = input()

    guess = int(guess)
    guessesTaken = guessesTaken + 1

    if guess < number:

        print('Your guess is too low.') # There are eight spaces in front of print.

    if guess > number:

        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:

    guessesTaken = str(guessesTaken)

    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:

    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
"""
