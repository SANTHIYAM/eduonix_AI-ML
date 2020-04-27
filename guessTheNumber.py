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
