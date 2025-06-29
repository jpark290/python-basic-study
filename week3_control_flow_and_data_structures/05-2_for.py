# 5-2. for loop

# while → best when you don’t know exactly how many times to repeat
# for → best when you know the exact number of iterations

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for day in days:
    print(f"Today is {day}.")

print("It's the weekend!")

# A string (not just a list) can be used in a for loop
days = "12345"

for day in days:
    print(f"Day {day}")

print("It's the 6th day now.")

# Warning: If using strings like "1day2day..."
# the loop splits each character → causes incorrect output
# Example:
# "1day2day" → '1', 'd', 'a', 'y', '2', 'd', 'a', 'y'
# Output:
# Day 1
# Day d
# Day a
# Day y
# Day 2
# Day d
# Day a
# Day y

# To avoid that, use a list or range instead

# Example using range (starts at 0 by default)
for i in range(11):  # 0 to 10
    print(f"Lap {i}")

print("Finished running.")

# To start from 1 instead of 0:
for i in range(1, 11):  # 1 to 10
    print(f"Lap {i}")

print("Finished running.")

# Accumulating total with for loop
num = 0
for i in range(1, 101):
    print(i)
    num = num + i  # adds each i to the total

print(num)  # 5050
