# Hangman Python Project
# In this Kylie Ying tutorial, you will learn how to work with dictionaries, lists, and nested if statements. You will also learn how to work with the string and random Python modules.

import random


words = ['python', 'hangman', 'developer', 'programming']

word = random.choice(words)
hidden_word = ['_' for _ in word]  

tries = 6

while tries > 0 and '_' in hidden_word:
    print(' '.join(hidden_word))  
    guess = input("Guess a letter: ").lower() 

    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                hidden_word[index] = guess  
        print(f"Good job! {guess} is in the word.")
    else:
        tries -= 1  
        print(f"Wrong guess! You have {tries} tries left.")

    print()

if '_' not in hidden_word:
    print("Congratulations, you won!")
else:
    print(f"Game over! The word was {word}.")
