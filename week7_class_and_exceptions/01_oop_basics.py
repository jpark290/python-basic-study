# OOP Basics - Example with StarCraft Units

# 1. Without using classes
name = "Marine"
hp = 40
damage = 5

print("{} unit created.".format(name))
print("HP: {}, Attack: {}".format(hp, damage))

tank_name = "Tank"
tank_hp = 150
tank_damage = 35

print("{} unit created.".format(tank_name))
print("HP: {}, Attack: {}".format(tank_hp, tank_damage))

# Simulate attacking
def attack(name, location, damage):
    print("{} attacks enemies towards {} direction. [Attack: {}]".format(name, location, damage))

attack(name, "1 o'clock", damage)
attack(tank_name, "1 o'clock", tank_damage)

# Adding another tank (redundant code)
tank2_name = "Tank"
tank2_hp = 150
tank2_damage = 35
print("{} unit created.".format(tank2_name))
print("HP: {}, Attack: {}".format(tank2_hp, tank2_damage))
attack(tank2_name, "1 o'clock", tank2_damage)

# Problem: As the number of units increases, code becomes repetitive and hard to manage


# 2. Using a class to define units
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} unit created.".format(self.name))
        print("HP: {}, Attack: {}".format(self.hp, self.damage))

marine1 = Unit("Marine", 40, 5)
marine2 = Unit("Marine", 40, 5)
tank1 = Unit("Tank", 150, 35)
tank2 = Unit("Tank", 150, 35)


# __init__ is a constructor automatically called when an object is created.
# self refers to the instance itself (used to access its attributes and methods).


# 3. Member Variables
wraith1 = Unit("Wraith", 80, 5)
print("Unit name: {}, Attack: {}".format(wraith1.name, wraith1.damage))
# You can access instance variables outside the class

wraith2 = Unit("Captured Wraith", 80, 5)
wraith2.cloaking = True  # Dynamically adds a new member variable

if wraith2.cloaking == True:
    print("{} is currently in cloaking mode.".format(wraith2.name))
# Note: wraith1 does not have the 'cloaking' variable → would raise an error


# 4. Methods inside a class
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{} attacks enemies towards {} direction. [Attack: {}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} took {} damage.".format(self.name, damage))
        self.hp -= damage
        print("{} now has {} HP.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} has been destroyed.".format(self.name))

# Create and simulate Firebat unit actions
firebat1 = AttackUnit("Firebat", 50, 16)
firebat1.attack("5 o'clock")
firebat1.damaged(25)
firebat1.damaged(25)
