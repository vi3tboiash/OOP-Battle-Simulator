import random
from enemy import Enemy

class Boss(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name, maxHP=250, attack_power=15)
        self.prize=0


    def LegSweep(self, hero):
        """Return a random amount of damage."""
        """Boss reduces hero damage"""
        hero.attack_power -= 5
        hero.health -= random.randint(1, self.attack_power*0.5)
        print(f"{hero.name}'s attack was decreased by 5!")

    def bigHit(self, hero):
        hero.health -= random.randint(5,self.attack_power)

    def explode(self, hero):
        boom = random.randint(0, self.maxHP/5)
        hero.health-= boom
        print(f"KABOOOMMMMMMM! \n{hero.name} took {boom} damage")


