# File Writing: Open in write mode ("w")
score_file = open("score.txt", "w", encoding="utf8")
# encoding="utf8" ensures proper handling of Korean/Unicode characters

print("Math: 0", file=score_file)
print("English: 50", file=score_file)
print("Coding: 100", file=score_file)
score_file.close()  # Always close the file after writing


# File Appending: Open in append mode ("a")
score_file = open("score.txt", "a", encoding="utf8")
# Appends new content to the existing file

score_file.write("Science: 80\n")
score_file.write("History: 90")
score_file.close()


# File Reading: Read entire content
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()


# File Reading: Read line by line using readline()
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())  # Reads one line and moves to the next
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()


# File Reading: Using a while loop for unknown line count
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:  # Stop when there's no more content
        break
    print(line, end="")  # Avoid extra newline
score_file.close()


# File Reading: Reading all lines at once as a list
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # Returns a list of lines

for line in lines:
    print(line, end="")

score_file.close()


# -------------------------------
# Using pickle for binary storage
# -------------------------------
# pickle: Saves Python objects to a binary file so they can be reused later

import pickle

# Write a Python dictionary to a binary file
profile_file = open("profile.pickle", "wb")  # wb = write binary
profile = {"name": "Haley", "age": 30, "hobbies": ["Soccer", "Basketball", "Coding"]}
print(profile)
pickle.dump(profile, profile_file)  # Serialize object to file
profile_file.close()

# Read the binary file back into Python
profile_file = open("profile.pickle", "rb")  # rb = read binary
profile = pickle.load(profile_file)  # Deserialize object
print(profile)
profile_file.close()


# Use 'with' to open a file (automatically closes it)
import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))


# Using 'with' without pickle for text files
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("I am studying Python diligently.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
