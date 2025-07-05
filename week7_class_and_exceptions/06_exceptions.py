# 1. Basic Exception Handling

try:
    print("Division-only calculator")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError as err:
    print(err)


# Handling list-based division (with a missing line)
try:
    print("Division-only calculator")
    nums = []
    nums.append(int(input("Enter the first number: ")))
    nums.append(int(input("Enter the second number: ")))
    # nums.append(int(nums[0] / nums[1]))  # ← If missing, leads to IndexError
    print("{} / {} = {}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError as err:
    print(err)
except:
    print("An unknown error occurred. Please try again.")

# OR (more informative):
# except Exception as err:
#     print("An unknown error occurred.")
#     print(err)


# 2. Raising Exceptions
try:
    print("Single-digit division-only calculator")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError("Please enter single-digit numbers only.")
    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("Invalid input. Only single-digit numbers are allowed.")


# 3. Custom Exception
class BignumberError(Exception):
    pass

try:
    print("Single-digit division-only calculator")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num1 >= 10 or num2 >= 10:
        raise BignumberError
    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("Invalid input. Only single-digit numbers are allowed.")
except BignumberError:
    print("Error occurred. Please enter only single-digit numbers.")


# Custom exception with detailed message
class BignumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("Single-digit division-only calculator")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num1 >= 10 or num2 >= 10:
        raise BignumberError("Invalid input values: {}, {}".format(num1, num2))
    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("Invalid input. Only single-digit numbers are allowed.")
except BignumberError as err:
    print("Error occurred. Please enter only single-digit numbers.")
    print(err)


# 4. finally Block
# Executes regardless of whether an exception occurred or not

try:
    print("Single-digit division-only calculator")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num1 >= 10 or num2 >= 10:
        raise BignumberError("Invalid input values: {}, {}".format(num1, num2))
    print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("Invalid input. Only single-digit numbers are allowed.")
except BignumberError as err:
    print("Error occurred. Please enter only single-digit numbers.")
    print(err)
finally:
    print("Thank you for using the calculator.")
