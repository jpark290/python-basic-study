# 3. Tuples (immutable sequences)
# ====================================================

food_tuple = ("pizza", "cheese", "meat", "steak", "soup")
print(type(food_tuple))
print(food_tuple[0])

# Slicing works
print(food_tuple[1:3])       # ('cheese', 'meat')

# uples are immutable; assignment raises TypeError
# food_tuple[0] = "google"  # ➜ TypeError

# Tuple operations
number1 = (1, 2)
number2 = (3, 4)
print(number1 + number2)     # concatenation
print(number1 * 2)           # repetition
print(len(number1))
# print(number1.index(1))    # methods exist but are limited