# 5-4. Using for loops with if statements

# 1. Even or odd
for i in range(1, 21):
    if i % 2 == 0:  # if divisible by 2 → even
        print(f"{i} is even.")
    else:
        print(f"{i} is odd.")

# 2. Multiples of 3
for i in range(1, 21):
    if i % 3 == 0:  # if divisible by 3
        print(f"{i} is a multiple of 3.")

# 3. Multiples of 3 and 5
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:  # divisible by both
        print(f"{i} is a multiple of both 3 and 5.")
    elif i % 3 == 0:
        print(f"{i} is a multiple of 3.")
    elif i % 5 == 0:
        print(f"{i} is a multiple of 5.")

# 🔍 Note:
# - Order matters in if-elif chains.
# - If we start with `if i % 3 == 0` first,
#   numbers like 15 or 30 will be printed as "multiple of 3" only,
#   because once an `elif` is true, the rest are skipped.
# - If we use `if` for all three blocks instead of `elif`,
#   all matching conditions will be evaluated → multiple outputs per number.