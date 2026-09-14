class Equipment:
    def __init__(self, name, Type, power):
            self.name = name
            self.type = Type
            self.power = power

    def add(self, entity):
        if self.type=="potion":
             entity.health = entity.health+self.power*5
             print(f"added {self.power*5} to {entity.name}'s health")
        elif self.type=="def":
             entity.armor = entity.armor + self.power
             print(f"added {self.power} to {entity.name}'s defense")
        elif self.type=="atk":
             entity.attack = entity.attack+self.power*2
             print(f"added {self.power*2} to {entity.name}'s power")
        else:
             entity.health = entity.health+10
             entity.armor = entity.armor+self.power*0.25
             entity.attack = entity.attack + self.power
             print(f"added 10 health, {self.power*0.25} defense, and {self.power} attack power to {entity.name}")
        
