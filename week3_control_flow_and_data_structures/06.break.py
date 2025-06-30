# 06. break and continue in loops

# while loop using a condition
count = 1

while count < 11:
    print(f"Lap {count}")
    count += 1

print("Finished running!")

# Infinite loop with break
count = 1

while True:
    print(f"Lap {count}")
    count += 1
    if count >= 10:
        break  # loop stops when count reaches 10

print("Finished running!")

# Using continue to skip an iteration
count = 0

while True:
    count += 1

    if count == 19:
        print("Taking a short break...")
        continue  # skip the rest of this iteration

    print(f"Lap {count}")

    if count == 20:
        break

print("Finished running!")

# break exits the entire loop
# continue skips the current iteration and proceeds to the next one

# Basic for loop
for i in range(20):
    print(i)  # prints 0–19

# break example
for i in range(20):
    if i == 5:
        break  # exits the loop when i == 5
    print(i)  # prints 0–4

# continue example
for i in range(20):
    if i == 5:
        continue  # skips printing 5
    print(i)  # prints 0–4 and 6–19
