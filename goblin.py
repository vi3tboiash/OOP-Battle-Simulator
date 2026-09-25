import random
from enemy import Enemy

class Goblin(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, health=100, attack_power=7)
        self.gold=0


    def stealGold(self, hero):
        """Return a random amount of damage."""
        """Gobbos taking hero's gold"""
        self.gold+=hero.gold
        hero.gold = 0
        print("YOU JUST GOT OWNED!")

