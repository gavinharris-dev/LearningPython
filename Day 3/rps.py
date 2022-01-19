from nis import match
import random

allowed_values = [
    {
        "title": "Rock", 
        "beats": "Scissors"
    }, {
        "title": "Paper", 
        "beats": "Rock"
    }, {
        "title": "Scissors", 
        "beats": "Paper"
    }]

myPick = random.choice(allowed_values)
yourPick = int(input("Pick one [0: Rock, 1: Paper, 2: Scissors]: "))

yourPick = allowed_values[yourPick]

print(yourPick, myPick)

if (yourPick["beats"] == myPick["title"] ):
    print("You win!")
elif (myPick["beats"] == yourPick["title"] ):
    print("I win")
else:
    print("Draw")

    
