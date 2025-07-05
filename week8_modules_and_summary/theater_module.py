# 1. Module Example
# Calculate ticket prices based on the number of people

# Regular price
def price(people):
    print("Ticket price for {} person(s): {} KRW".format(people, people * 10000))

# Morning discount price
def price_morning(people):
    print("Morning discount price for {} person(s): {} KRW".format(people, people * 6000))

# Military discount price
def price_military(people):
    print("Military discount price for {} person(s): {} KRW".format(people, people * 4000))
