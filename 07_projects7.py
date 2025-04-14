# Project 7: Password Generator Python Project

import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))  
    return password

num_passwords = int(input("How many passwords do you want to generate? "))
length = int(input("Enter the length of the passwords: "))

for _ in range(num_passwords):
    print(generate_password(length))

# is ki practice krni h.7451