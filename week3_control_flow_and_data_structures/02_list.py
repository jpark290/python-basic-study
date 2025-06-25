# 2. Lists (mutable sequences)

food = []
print(type(food))            # <class 'list'>

food = ["pizza", "soup", "icecream", "burger"]
print(len(food))             # 4
print(type(food[0]))         # str

# List can contain mixed types
food = [100, "soup", "icecream", "burger"]
print(type(food[0]))         # int

# Nested list
food = ["pizza", ["soup", "icecream"], "burger"]
print(food[1])               # ['soup', 'icecream']
print(food[1][0])            # 'soup'

# List concatenation & repetition
food2 = ["rice", "potato"]
print(food + food2)
print((food + food2) * 3)

# Common list methods
food = ["ramen", "meat"]
food.append("pizza")
print(food)                  # ['ramen', 'meat', 'pizza']

food.insert(1, "salad")
print(food)                  # ['ramen', 'salad', 'meat', 'pizza']

food.remove("ramen")        # removes first matching item
print(food)

food = ["ramen", "meat", "ramen"]
food.remove("ramen")         # only first 'ramen' removed
print(food)

print(food.count("ramen"))   # count occurrences
print(food.index("meat"))    # first index of 'meat'

food.sort()                  # ascending
print(food)
food.sort(reverse=True)      # descending
print(food)

food[0] = "potato"           # lists are mutable
print(food)