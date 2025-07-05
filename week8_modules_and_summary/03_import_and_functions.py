# 1. pip install
# Example usage of external module: BeautifulSoup

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip commands:
# pip list                → Show installed packages
# pip show <package>      → Show details of a specific package
# pip install --upgrade <package> → Upgrade to latest version
# pip uninstall <package> → Uninstall the package


# 2. Built-in Functions

# input(): get user input
language = input("What is your favorite programming language? ")
print(f"Your favorite language is {language}.")

# dir(): show attributes and methods of an object
print(dir())  # List current module's symbols (no random yet)

import random
print(dir())  # Now includes 'random'

import pickle
print(dir())  # Now includes 'pickle'

# To see available methods in a specific module
print(dir(random))

# list object methods
lst = [1, 2, 3]
print(dir(lst))

# string object methods
name = "Jim"
print(dir(name))


# 3. External Modules (Standard Library)

# glob: file & folder listing (similar to dir command)
import glob
print(glob.glob("*.py"))  # All .py files in current directory

# Use full path
files = glob.glob("week8_modules_and_summary/*.py")
print(files)

# os: access to OS-level functions
import os
print(os.getcwd())  # Current working directory

folder = "sample_dir"
if os.path.exists(folder):
    print("Folder already exists.")
    os.rmdir(folder)
    print(f"Deleted folder: {folder}")
else:
    os.makedirs(folder)
    print(f"Created new folder: {folder}")

# list directory contents
print(os.listdir())  # Files and folders in current directory


# time: time-related functions
import time
print(time.localtime())  # Current time as struct
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


# datetime: date and time
import datetime
print("Today's date is", datetime.date.today())

# timedelta: time difference
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("100 days from today:", today + td)
