# 04_Class
# A class is a blueprint for creating something.
# An object is an instance created from that class.

class User:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def hello(self):  # Method
        print("Hello")

# The __init__ method runs automatically when an object is created from the class.
# What is a method? It's something you use with a dot after an object, like temp.append(1).
# For example, list is a class, and append is a method belonging to that class.
# Methods can only be used on ~instances created from a class.

user_1 = User("Haley", 20)  # Create an instance of the User class
# An object named user_1 is created.
# If one of the required values is missing, the code will raise an error.
# You must provide all arguments defined in __init__.

user_1.hello()  # Call the hello method of the User class

# ------------------------------

class User:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def hello(self):  # Method
        print(f"Hello, my name is {self.name}")

user_1 = User("Haley", 20)
user_2 = User("John", 25)

user_1.hello()
user_2.hello()

print(user_1.name)
print(user_1.age)

print(user_2.name)
print(user_2.age)

temo = [1, 2, 3, 4, 5]
print(type(temo))     # <class 'list'>
print(type(user_1))   # <class '__main__.User'>
# This confirms that user_1 is created from a class
