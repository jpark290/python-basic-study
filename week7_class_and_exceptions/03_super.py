# 4. super()
# Use super() to call a method from the parent class more concisely.

# Example (commented out):
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         super().__init__(name, hp, 0)
#         # Parent constructor is called via super(), self is omitted
#         self.location = location


# What happens with multiple inheritance?

class Unit:
    def __init__(self):
        print("Unit constructor called")


class Flyable:
    def __init__(self):
        print("Flyable constructor called")
        super().__init__()


class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()  # Only calls Unit's constructor due to MRO (method resolution order)


# Create instance
dropship = FlyableUnit()
# Output:
# Unit constructor called
# Even though Flyable has super(), only Unit's constructor is executed


# Now reverse the inheritance order
class Unit:
    def __init__(self):
        print("Unit constructor called")


class Flyable:
    def __init__(self):
        print("Flyable constructor called")
        super().__init__()


class FlyableUnit(Unit, Flyable):
    def __init__(self):
        Flyable.__init__(self)
        Unit.__init__(self)
        # To ensure both parent constructors are called,
        # you must explicitly call them when using multiple inheritance.


# Create another instance
dropship = FlyableUnit()
# Output:
# Flyable constructor called
# Unit constructor called
