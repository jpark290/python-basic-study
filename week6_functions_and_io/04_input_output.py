# Standard Output with Custom Separators and Endings
print("Python", "Java", sep=", ")
print("Python", "Java", sep=" vs ")

print("Python", "Java", sep=", ", end="?")
print("What is your favorite language?")
# Output appears on the same line due to custom 'end' parameter


# Writing to stdout and stderr
import sys
print("Python", "Java", file=sys.stdout)   # Normal output
print("Python", "Java", file=sys.stderr)   # Error output
# Useful when separating logs and errors (e.g., for debugging or logging)


# Dictionary output
scores = {"Math": 0, "English": 50, "Coding": 100}
for subject, score in scores.items():
    print(subject, score)

# Aligning text for better formatting
scores = {"Math": 0, "English": 50, "Coding": 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=": ")
# ljust(8): left-justify with width 8
# rjust(4): right-justify with width 4


# Queue Number Formatting
# Output: 001, 002, ..., 020
for num in range(1, 21):
    print("Queue Number: " + str(num).zfill(3))
# zfill(3): pads numbers with zeros to make them 3 digits


# Standard Input
answer = input("Enter any value: ")
print("You entered: " + answer)
# Note: input() always returns a string


# -------------------------
# Various Output Formatting
# -------------------------

# Right-align with spaces, width = 10
print("{0: >10}".format(500))

# Include sign for positive and negative numbers
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# Left-align, fill with underscore, show sign
print("{0:_<+10}".format(500))

# Add commas every 3 digits
print("{0:,}".format(1000000000))

# Add commas and sign
print("{0:+,}".format(1000000000))

# Add commas, sign, total width 30, fill with ^
print("{0:^<+30,}".format(10000000000000))

# Floating-point output
print("{0:f}".format(5 / 3))        # Full float
print("{0:.2f}".format(5 / 3))      # Rounded to 2 decimal places
