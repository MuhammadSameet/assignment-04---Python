# Countdown Timer Python Project
# In this Code With Tomi tutorial, you will learn how to build a countdown timer using the time Python module. This is a great beginner project to get you used to working with while loops in Python.

import time  

countdown_time = 10

while countdown_time > 0:
    print(countdown_time) 
    time.sleep(1)  
    countdown_time -= 1 

print("Time's up!")
