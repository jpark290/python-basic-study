# Quiz 1) Randomly select a date for an offline coding study session.

# Conditions:
# 1. The date must be chosen randomly.
# 2. To account for different month lengths, the range is limited to the minimum (28 days).
# 3. Days 1 to 3 are excluded due to preparation.

from random import *
study_date = randint(4, 28)
print(f"Offline study meeting will be held on the {study_date}th of every month.")


# Quiz 2) Generate a password based on a website URL.

# Example input: "http://google.com"
# Rules:
# 1. Remove "http://"
# 2. Ignore everything after the first dot (.)
# 3. Create a password using: first 3 letters + length of remaining string + number of 'e' + "!"

site = "http://github.com"
my_str = site.replace("http://", "")         # Remove protocol
my_str = my_str[:my_str.index(".")]          # Trim at the first dot
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + "!"
print(f"Generated password: {password}")


# Quiz 3) Randomly select giveaway winners from users who commented.

# Conditions:
# 1. There are 20 commenters, IDs 1 to 20.
# 2. Winners are chosen randomly without duplicates.
# 3. Use shuffle and sample from the random module.

from random import *
users = list(range(1, 21))  # Create a list of user IDs from 1 to 20
shuffle(users)              # Shuffle the list

# Incorrect example (may contain duplicates)
print(f"Chicken winner: {sample(users, 1)}")
print(f"Coffee winners: {sample(users, 3)}")

# Correct example (no duplicates)
winners = sample(users, 4)
print("-- Winner Announcement --")
print(f"Chicken winner: {winners[0]}")
print(f"Coffee winners: {winners[1:]}")


# Quiz 4) As a taxi driver using Cocoa service, count how many passengers are matched.

# Conditions:
# 1. Each passenger has a random ride time between 5 and 50 minutes.
# 2. Only passengers with ride time between 5 and 15 minutes are accepted.

# Output example:
# [O] 1st passenger (Time: 15 min)
# [ ] 2nd passenger (Time: 50 min)
# ...
# Total passengers matched: X

from random import *
count = 0  # Total matched passengers

for i in range(1, 51):  # Passenger numbers 1 to 50
    time = randrange(5, 51)  # Ride time between 5 and 50 minutes
    if 5 <= time <= 15:
        print(f"[O] Passenger {i} (Time: {time} min)")
        count += 1
    else:
        print(f"[ ] Passenger {i} (Time: {time} min)")

print(f"Total passengers matched: {count}")
