import random
class Hero:
    """The hero blueprint will be implemented later in the project."""
    def __init__(self, name, hero_role):
        self.name = name
        self.hero_role = hero_role
        if hero_role == "barbarian":
            self.health = 100
            self.attack_power = 25
        elif hero_role == "mage":
            self.health = 75
            self.attack_power = 40
        elif hero_role == "knight":
            self.health = 150
            self.attack_power = 10
        elif hero_role == "default":
            self.health = 130
            self.attack_power = 15


    def attack(self):
        return random.randint(1,self.attack_power)

    def take_damage(self, damage):
        self.health=max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0
