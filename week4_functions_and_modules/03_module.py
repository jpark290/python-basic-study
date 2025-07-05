# 03_Module
# A module is a file that contains Python code for specific functionality
# There are many modules in Python; here we will explore a few basic ones

# How to import a module
import time
print(1)
time.sleep(2)  # Pauses the program for 2 seconds using the time module
print(2)

import time
for i in range(1, 11):
    print(f"{i} : hi!")
    time.sleep(1)  # Waits for 1 second between each line

# Using the random module to generate random numbers
import random

x = random.random()
print(x)  # Prints a random float between 0.0 and 1.0

x = random.randint(1, 10)
print(x)  # Prints a random integer between 1 and 10 (inclusive)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(x)
print(x)  # Shuffles the list in place

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = random.choice(x)
print(y)  # Randomly selects one element from the list

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = random.sample(x, 3)
print(y)  # Randomly selects 3 unique elements from the list

# Working with dates and times using the datetime module
import datetime

today = datetime.date.today()
print(today)        # Prints today's date in YYYY-MM-DD format
print(today.month)  # Prints the current month as a number (1–12)

# Using the os module for file system operations
import os
print(os.getcwd())    # Prints the current working directory
print(os.listdir())   # Lists files and directories in the current directory
