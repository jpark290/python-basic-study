# Define a function to open a new bank account
def open_account():
    print("A new account has been created.")


# Define a deposit function
def deposit(balance, money):
    print(f"Deposit completed. New balance is {balance + money} KRW.")
    return balance + money


# Example usage of deposit
balance = 0
balance = deposit(balance, 1000)
print(balance)  # Print updated balance


# Define a withdrawal function
def withdraw(balance, money):
    if balance >= money:
        print(f"Withdrawal completed. New balance is {balance - money} KRW.")
        return balance - money
    else:
        print(f"Insufficient funds. Current balance is {balance} KRW.")
        return balance


# Test withdrawal scenarios
balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)  # Should print insufficient funds
balance = withdraw(balance, 500)   # Should succeed


# Define a night-time withdrawal function with commission
def withdraw_night(balance, money):
    commission = 100  # Fixed commission fee
    return commission, balance - money - commission


# Example usage of night withdrawal
balance = 0
balance = deposit(balance, 1000)
commission, balance = withdraw_night(balance, 500)
print(f"Commission: {commission} KRW, Balance: {balance} KRW")


# Function with positional arguments
def profile(name, age, main_lang):
    print(f"name: {name}")
    print(f"age: {age}")
    print(f"main_lang: {main_lang}")


# Call with full arguments
profile("Haley", 20, "Python")
profile("John", 25, "JavaScript")


# Function with default arguments
def profile(name, age=20, main_lang="Python"):
    print(f"name: {name}")
    print(f"age: {age}")
    print(f"main_lang: {main_lang}")


# Call using default values
profile("Haley")
profile("John")


# Function using keyword arguments
def profile(name, age, main_lang):
    print(name, age, main_lang)


# Call with keyword arguments (order doesn't matter)
profile(name="Haley", main_lang="Python", age=20)
profile(main_lang="JavaScript", age=25, name="John")
