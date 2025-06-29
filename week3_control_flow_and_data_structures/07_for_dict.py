# 07.for_dict.py
# Looping through dictionaries

user_data = {"name": "Alice", "age": 30, "email": "alice@example.com"}

# Iterating over dictionary keys (default behavior)
for key in user_data:
    print(key)
# Output:
# name
# age
# email

# Accessing a specific value by key
print(user_data["name"])  # Alice

# Iterating over keys and using them to get values
for key in user_data:
    print(user_data[key])
# Output:
# Alice
# 30
# alice@example.com

# Displaying both key and value together
for key in user_data:
    print(f"{key}: {user_data[key]}")
# Output:
# name: Alice
# age: 30
# email: alice@example.com

# Using .items() to get key-value pairs as tuples
for item in user_data.items():
    print(item)
# Output:
# ('name', 'Alice')
# ('age', 30)
# ('email', 'alice@example.com')