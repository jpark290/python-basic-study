# 4. Dictionaries

# A dictionary is a collection of key-value pairs
user = {
    "name": "Haley",
    "job": "programmer",
    "email": "Haley@mail.com"
}

# Any data type can be a value (int, list, etc.)
example = {"height": 170}
print(user["job"])           # 'programmer'

# Add a new key-value pair
user["age"] = 15
print(user)  # {'name': ..., 'job': ..., 'email': ..., 'age': 15}

# Delete a key-value pair
del user["name"]
print(user)  # {'job': ..., 'email': ..., 'age': ...}

# Keys in a dictionary must be unique – duplicates will be overwritten

# Get only keys
key_list = user.keys()
print(key_list)              # dict_keys([...])
print(type(key_list))        # <class 'dict_keys'>
# Note: dict_keys is not a list. It's a special view object.
# It behaves like a list in many ways but doesn’t support all list methods.

# Convert to list to use list methods
key_list = list(key_list)

# Get only values
value_list = user.values()
print(value_list)            # dict_values([...])
print(type(value_list))      # <class 'dict_values'>
# dict_values is also not a real list (same as above)

# Get all key-value pairs
item_list = user.items()
print(item_list)             # dict_items([(...), (...), ...])
print(type(item_list))       # <class 'dict_items'>
# dict_items is a view object showing key-value pairs as tuples

# Convert to list of tuples
item_list = list(item_list)
print(item_list)
print(type(item_list))       # <class 'list'>
print(item_list[0])          # ('job', 'programmer')
print(type(item_list[0]))    # <class 'tuple'>