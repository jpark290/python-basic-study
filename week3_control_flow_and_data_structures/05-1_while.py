# 5. while Loops

# while <condition>:
#     code1
#     code2
#     ...
# Executes repeatedly *as long as* the condition is True (like an if statement that loops)

# Example: counting laps while running around a track

# Infinite loop example (be careful!)
count = 1
while True:
    print(f"Lap {count}")
    count = count + 1
# This loop never ends unless you stop the program manually (Ctrl + C)

# Loop with a stopping condition (count < 11 → stops when count reaches 11)
count = 1
while count < 11:
    print(f"Lap {count}")
    count = count + 1

print("Finished running.")
# Output: Lap 1 to Lap 10, then "Finished running."

# Same loop using += (shorthand for count = count + 1)
count = 1
while count < 11:
    print(f"Lap {count}")
    count += 1