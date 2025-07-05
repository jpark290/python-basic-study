from random import *

# -----------------------------
# Base Unit Class
# -----------------------------
class Unit:
    def __init__(self, name, hp, speed):   
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{self.name} unit created.")

    def move(self, location):
        print(f"{self.name} moves toward {location}. [Speed: {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} took {damage} damage.")
        self.hp -= damage
        print(f"{self.name} current HP: {self.hp}")
        if self.hp <= 0:
            print(f"{self.name} has been destroyed.")


# -----------------------------
# Attack Unit (inherits Unit)
# -----------------------------
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        super().__init__(name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} attacks enemies at {location}. [Damage: {self.damage}]")


# -----------------------------
# Specific Units
# -----------------------------

class Marine(AttackUnit):
    def __init__(self):
        super().__init__("Marine", 40, 1, 5)

    def stimpack(self):
        if self.hp >= 10:
            self.hp -= 10
            print(f"{self.name} uses Stimpack. (HP -10)")
        else:
            print(f"{self.name} has insufficient HP to use Stimpack.")


class Tank(AttackUnit):
    seize_developed = False  # Class variable: whether siege mode is available

    def __init__(self):
        super().__init__("Tank", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if not Tank.seize_developed:
            return
        if not self.seize_mode:
            print(f"{self.name} switches to Siege Mode.")
            self.damage *= 2
            self.seize_mode = True
        else:
            print(f"{self.name} exits Siege Mode.")
            self.damage /= 2
            self.seize_mode = False


# -----------------------------
# Flying Units
# -----------------------------
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, location):
        print(f"{self.name} flies toward {location}. [Flying Speed: {self.flying_speed}]")


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # ground speed = 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(location)


class Wraith(FlyableAttackUnit):
    def __init__(self):
        super().__init__("Wraith", 80, 20, 5)
        self.cloaking = False

    def toggle_cloaking(self):
        if self.cloaking:
            print(f"{self.name} deactivates Cloaking.")
            self.cloaking = False
        else:
            print(f"{self.name} activates Cloaking.")
            self.cloaking = True


# -----------------------------
# Game Flow Functions
# -----------------------------

def game_start():
    print("[Notice] New game started!")

def game_over():
    print("Player : gg")
    print("[Player] has left the game.")


# -----------------------------
# Game Script Begins
# -----------------------------
game_start()

# Create units
m1, m2, m3 = Marine(), Marine(), Marine()
t1, t2 = Tank(), Tank()
w1 = Wraith()

# Manage all units in a list
attack_units = [m1, m2, m3, t1, t2, w1]

# Move all units to a location
for unit in attack_units:
    unit.move("1 o'clock")

# Develop siege mode
Tank.seize_developed = True
print("[Notice] Tank Siege Mode has been developed.")

# Prepare each unit for attack mode
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.toggle_cloaking()

# All units attack
for unit in attack_units:
    unit.attack("1 o'clock")

# All units take damage
for unit in attack_units:
    unit.damaged(randint(5, 20))

# End game
game_over()
