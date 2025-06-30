# 5-3. Multiplication Table with for loops

# Step 1: Check the range (2 to 9)
for i in range(2, 10):
    print(i)

# Step 2: Nested loops to build the table
for i in range(2, 10):  # Outer loop: 2 to 9
    print(f"<< {i} times table >>")
    for j in range(1, 10):  # Inner loop: 1 to 9
        result = i * j
        print(f"{i} * {j} = {result}")

# Explanation:
# When i = 2, j goes from 1 to 9 → prints 2 * 1 to 2 * 9
# When i = 3, j again goes from 1 to 9 → prints 3 * 1 to 3 * 9
# ... and so on until i = 9

print("Multiplication table completed.")