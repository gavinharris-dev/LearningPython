import numbers
import random

number = random.randint(0, 10)
guess = None

while guess != number:
    guess = int(input("Guess: "))

    if guess == number:
        print("You got it!")
        break
    elif guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
