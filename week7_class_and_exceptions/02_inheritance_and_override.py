# 1. Inheritance (상속)

# Base class: General unit (e.g., Medic - no attack capability)
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# Separate class for attack units
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} attacks enemies towards {location}. [Damage: {self.damage}]")

# Duplicate code → Use inheritance

# AttackUnit now inherits from Unit
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)  # Call parent constructor
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} attacks enemies towards {location}. [Damage: {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} took {damage} damage.")
        self.hp -= damage
        print(f"{self.name} current HP: {self.hp}")
        if self.hp <= 0:
            print(f"{self.name} has been destroyed.")

# Create unit and simulate attack and damage
firebat1 = AttackUnit("Firebat", 50, 16)
firebat1.attack("5 o'clock")
firebat1.damaged(25)
firebat1.damaged(25)


# 2. Multiple Inheritance (다중 상속)

# Class for flying capability
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} flies towards {location}. [Flying speed: {self.flying_speed}]")


# Airborne attacking unit
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# Valkyrie: air unit with rapid fire
valkyrie1 = FlyableAttackUnit("Valkyrie", 200, 6, 5)
valkyrie1.fly(valkyrie1.name, "3 o'clock")


# Method Overriding (메서드 오버라이딩)

# Updated Unit class with move method
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[Ground Unit Moving]")
        print(f"{self.name} moves to {location}. [Speed: {self.speed}]")


# AttackUnit inherits move from Unit
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} attacks enemies towards {location}. [Damage: {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} took {damage} damage.")
        self.hp -= damage
        print(f"{self.name} current HP: {self.hp}")
        if self.hp <= 0:
            print(f"{self.name} has been destroyed.")


# Redefine FlyableAttackUnit with overridden move()
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # Ground speed = 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[Air Unit Moving]")
        self.fly(self.name, location)

# Example usage
vulture1 = AttackUnit("Vulture", 80, 10, 20)            # Ground unit
battlecruiser1 = FlyableAttackUnit("Battlecruiser", 500, 25, 3)  # Air unit

vulture1.move("11 o'clock")
battlecruiser1.move("9 o'clock")


# 3. pass Statement

# pass = Do nothing (placeholder for future implementation)
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

# Supply Depot: building unit, supports 8 unit capacity
supply_depot = BuildingUnit("Supply Depot", 500, "7 o'clock")

# Placeholder functions
def game_start():
    print("Starting a new game...")

def game_over():
    pass  # Game over logic to be implemented later

game_start()
game_over()
