# Example of using fixed number of arguments (not flexible)

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print(f"name: {name}")
    print(f"age: {age}")
    print(lang1, lang2, lang3, lang4, lang5)

# Must always pass 5 languages (even empty strings)
profile("Haley", 20, "Python", "Java", "C", "C++", "JavaScript")
profile("John", 25, "Kotlin", "Swift", "", "", "")

# → Not flexible: must match exact number of arguments.


# Example using *args (variable-length arguments)

def profile(name, age, *language):
    print(f"name: {name}")
    print(f"age: {age}")
    for lang in language:
        print(lang, end=' ')
    print()  # for newline

# Now you can pass any number of language arguments
profile("Haley", 20, "Python", "Java", "Swift", "C", "C++", "JavaScript")
profile("John", 25, "Kotlin", "Swift")


# ------------------------------
# Variable Scope (Local vs Global)
# ------------------------------

gun = 10  # global variable

def checkpoint(soldiers):
    gun = 20  # local variable (not the same as global 'gun')
    gun = gun - soldiers
    print(f"Remaining guns inside checkpoint: {gun}")

print(f"Total guns (global): {gun}")
checkpoint(2)  # Uses local 'gun' only
print(f"Total guns after checkpoint: {gun}")  # Still prints global 'gun' = 10

# Explanation:
# - 'gun = 20' inside the function creates a **local variable**
# - It does NOT affect the global 'gun'
# - Using only 'print(gun)' inside the function without initializing would raise an error


# Example using global variable (not recommended for larger codebases)

gun = 10

def checkpoint(soldiers):
    global gun  # use global variable
    gun = gun - soldiers
    print(f"Remaining guns (global): {gun}")

print(f"Total guns before checkpoint: {gun}")
checkpoint(2)  # Updates the global 'gun'
print(f"Total guns after checkpoint: {gun}")

# Caution: Using global variables makes the code harder to maintain and debug


# Recommended approach: pass and return values explicitly

gun = 10

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print(f"Remaining guns inside function: {gun}")
    return gun  # return the updated value

print(f"Total guns before checkpoint_ret: {gun}")
gun = checkpoint_ret(gun, 2)  # update global 'gun' by assigning return value
print(f"Total guns after checkpoint_ret: {gun}")
