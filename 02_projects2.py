# Guess the Number Game Python Project (computer)
# In this Kylie Ying tutorial, you will learn how to work with Python's random module, build functions, work with while loops and conditionals, and get user input.

import random

def number_game():
    number = random.randint(1, 100)
    guess = None

    while guess != number:
        guess = int(input("Guess the number between 1 to 100: "))

        if guess > number:
            print(f"Your no: {guess} is too hige, Try Again")
        elif guess < number:
            print(f"Your no: {guess} is too low, Try Again")
        else:
            print(f"COngratulation! You guess is right no: {number}")

number_game()