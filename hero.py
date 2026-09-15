import random
class Hero:
    """The hero blueprint will be implemented later in the project."""
    def __init__(self, name, hero_role):
        self.name = name
        self.armor = 0
        self.equipAmt = 0
        self.equipList = []
        self.hero_role = hero_role
        # defining how hero_role changes your hero
        if hero_role == "barbarian":
            self.maxHP = 100
            self.attack_power = 25
            self.equipMax = 3
        elif hero_role == "mage":
            self.maxHP = 65
            self.attack_power = 40
            self.equipMax = 5
        elif hero_role == "knight":
            self.maxHP = 150
            self.attack_power = 10
            self.equipMax = 4
        elif hero_role == "default":
            self.maxHP = 130
            self.attack_power = 15
            self.equipMax = 3
        self.health=self.maxHP

    def attack(self):
        return random.randint(1,self.attack_power)

    def take_damage(self, damage):
        self.health=max(0, self.health - max(0, damage-self.armor))
        print(f"{self.name} takes {damage} damage. Their armor defends {self.armor} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0

