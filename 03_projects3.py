# Guess the Number Game Python Project (user)
# In this Kylie Ying tutorial, you will build a guessing game where the computer has to guess the correct number. You will work with Python's random module, build functions, work with while loops and conditionals, and get user input.

import random

def computer_guess():
    while True:
        computer_guess = random.randint(1, 100) 
        print(f"Think of a number between 1 and 100, and I'll try to guess it!")
        
        feedback = "" 
        
        while feedback != "c":  

            print(f"Is your number {computer_guess}?")
            feedback = input("Enter your feedback (h for high, l for low, c for correct): ").lower()
            
            if feedback == "c":
                print("Yay! I guessed your number correctly.")
            elif feedback == "h":
                print("Your number is lower. I'll guess again.")
                computer_guess = random.randint(1, computer_guess - 1) 

            elif feedback == "l":
                print("Your number is higher. I'll guess again.")
                computer_guess = random.randint(computer_guess + 1, 100) 

computer_guess()
