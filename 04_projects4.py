# Rock, paper, scissors Python Project
# In this Kylie Ying tutorial, you will work with random.choice(), if statements, and getting user input. This is a great project to help you build on the fundamentals like conditionals and functions.

import random

# Rock, Paper, Scissors
def play():
    user = input("Choose one option (rock, paper, or scissors): ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You win!"

    return "You lose!"


def is_win(user, computer):
    return (
        (user == 'rock' and computer == 'scissors') or
        (user == 'scissors' and computer == 'paper') or
        (user == 'paper' and computer == 'rock')
    )

print(play())

