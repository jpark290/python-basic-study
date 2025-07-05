# Quiz) A popular chicken restaurant has long wait lines.
# To reduce wait time, an automatic ordering system was created.
# Update the code below to handle exceptions properly.

# Requirements:
# 1. If the input is less than 1 or not a number, handle with ValueError.
#    → Message: "Invalid input."
# 2. Only 10 chickens are available in total.
#    If sold out, raise a custom exception SoldOutError and terminate the program.
#    → Message: "Out of stock. No more orders can be taken."

# Custom exception
class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1  # Waiting number starts at 1

while True:
    try:
        print(f"[Remaining chicken: {chicken}]")
        order = int(input("How many chickens would you like to order? "))

        if order > chicken:
            print("Not enough ingredients.")
        elif order <= 0:
            raise ValueError
        else:
            print(f"[Waiting No. {waiting}] Order for {order} chicken(s) confirmed.")
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except SoldOutError:
        print("Out of stock. No more orders can be taken.")
        break
