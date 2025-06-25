# 1. if / elif / else statements

today = "sunday"

if today == "monday":
    print("Go to work")
elif today == "sunday":
    print("Day off!")

# Only the first True branch executes in an if–elif chain.
# Two independent if’s would both run if their conditions are True.

today = "saturday"
if today == "monday":
    print("Go to work")
elif today == "sunday":
    print("Day off!")
else:
    print("What's the day?")

# Numeric comparison example
num = 29
if num >= 30:
    print("Big")
elif num == 30:
    print("Exactly 30")
else:
    print("Small")

# Boolean variables as conditions
pizza = True
hamburger = False

if pizza:
    print("Yeah~")
elif hamburger:
    print("Wow")
else:
    print("So hungry")

# Note: in an if–elif chain only the first True branch runs.
# Two separate if’s evaluate independently.

pizza = True
hamburger = True
if pizza:
    print("Yeah~")
if hamburger:
    print("Wow")     # executes as well
else:
    print("So hungry")

# Truthy / falsy values examples
pizza = ""          # empty string ➜ False
hamburger = False
if pizza:
    print("Yeah~")
elif hamburger:
    print("Wow")
else:
    print("So hungry")

pizza = " "          # space char ➜ True
if pizza:
    print("Yeah~")

pizza = -1            # non‑zero numbers are True
if pizza:
    print("Yeah~ (numeric True)")

# Logical operators
pizza = True
hamburger = True
if pizza and hamburger:
    print("Two dishes, Yeah~")
elif hamburger:
    print("Wow")
else:
    print("So hungry")

pizza = False
if pizza or hamburger:
    print("At least one dish – Yeah!")

# not operator
offer_pizza = False
if not offer_pizza:
    print("No pizza today…")