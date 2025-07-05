# 02_def, return
# Creating functions and understanding return values

def add(a, b):
    print(f"{a} and {b} were received as input.")
    print(f"The sum of the two values is {a + b}.")

add(5, 6)     # Call the function with arguments 5 and 6
add(10, 20)   # Call the function with arguments 10 and 20
add(100, 200) # Call the function with arguments 100 and 200
add(1, 2)     # Call the function with arguments 1 and 2

# Using a function is much more efficient than entering values manually each time

# There are two main types of functions:
# 1. Functions that only perform actions (side effects)
# 2. Functions that return values

a = print("Hi!")
b = input("input: ")

print(a)  # print() does not return a value, so 'a' stores None
print(b)  # input() returns the user input, so 'b' stores the entered value

# Explanation:
# print() only outputs to the console and returns None
# input() returns the value entered by the user

def add(a, b):
    print(f"{a} and {b} were received as input.")
    print(f"The sum of the two values is {a + b}.")

temp = add(5, 10)
print(temp)  # This prints None because the function does not return a value

# To make the function return a value, use the return statement

def add(a, b):
    print(f"{a} and {b} were received as input.")
    print(f"The sum of the two values is {a + b}.")
    return a + b

temp = add(5, 10)
print(temp)  # This prints the result of 5 + 10 because the function now returns a value

# Why is return needed?

def add(a, b):
    print(f"{a} and {b} were received as input.")
    print(f"The sum of the two values is {a + b}.")
    return a + b

temp = add(5, 10)

add(temp, 100)  # Call the function again using the previous result and 100

# This code calls the add function with the result of the previous addition
# and passes that value along with 100 to calculate a new sum

# Important:
# If return comes before print inside a function,
# the function ends immediately and the code after return does not execute
# However, the return value still exists
