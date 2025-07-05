# 01_Built-in functions
name = input("Enter your name: ")

print(name)

print(len(name))  # Get the length of the input string

print(type(int("1234")))  # Check the type after converting string to integer
print(type(str(1234)))    # Check the type after converting integer to string

num = [1, 100, -9, 54, -4]

print(max(num))  # Find the maximum value in the list
print(min(num))  # Find the minimum value in the list

# max() and min() also work with strings, not just numbers
num = ["A", "z", "t", "u", "Y"]

print(max(num))  # Find the maximum value based on ASCII
print(min(num))  # Find the minimum value based on ASCII

num = "asdaTAXH"

print(max(num))  # Find the maximum character in the string (by ASCII)
print(min(num))  # Find the minimum character in the string (by ASCII)

# There are also functions to sort lists
num = [1, 100, -9, 54, -4]
print(sorted(num))  # Return a new sorted list (ascending order)

num = ["A", "z", "t", "u", "Y"]
print(sorted(num))  # Sort the list of characters alphabetically
print(sorted(num, reverse=True))  # Sort the list in reverse order

range(1, 11)  # Create a range object from 1 to 10
temp = list(range(1, 11))  # Convert the range object to a list

print(temp)
# When manually creating a list is tedious, you can use range()