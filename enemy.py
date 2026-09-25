import random


class Enemy:
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name, health = 50, attack_power = 4):
        self.name = name
        self.armor = 0
        self.equipAmt = 0
        self.maxHP = health
        self.health = self.maxHP
        self.attack_power = attack_power
        self.equipList = []
        self.inventory = []

    def attack(self):
        """Return a random amount of damage."""
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        """Return True while the goblin has health remaining."""
        return self.health > 0
