from goblin import Goblin
from hero import Hero
from equipment import Equipment
ARENA_NAME = "The Steel Cage"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Grubenstein")

    goblin2 = Goblin("Gobsmacker")

    hero = Hero("Slunges", "mage")
    armor = Equipment("shield", "def", 5)
    armor.add(hero)
    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print(f"But {hero.name} answers the call!")
    goblin.take_damage(hero.attack())
    hero.take_damage(goblin2.attack())
if __name__ == "__main__":
    main()
