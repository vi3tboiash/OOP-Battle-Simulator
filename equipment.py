class Equipment:
     def __init__(self, name, Type, power):
          self.name = name
          self.type = Type
          self.power = power

     def add(self, entity):
          if self.type != "potion":
               entity.equipAmt = entity.equipAmt+1
          if entity.equipAmt > entity.equipMax:
               print(f"{entity.equipList}")
          if input("You have max equipment! would you like to trade one out? (y/n)").lower() == "y":
               slot = input("which slot would you like to switch out?")
               removed = entity.equipList[slot]
               entity.equipList[slot]=self.name
               if removed.type=="armor":
                    entity.armor= entity.armor-removed.power
               elif removed.type=="atk":
                    entity.attack = entity.attack-removed.power*2
               else:
                    entity.maxHP = entity.maxHP-10
                    entity.armor = entity.armor-removed.power*0.25
                    entity.attack = entity.attack - removed.power

          if self.type=="potion":
               print(f"added {self.power*5} to {entity.name}'s health")
          elif self.type=="def":
               entity.armor = entity.armor + self.power
               print(f"added {self.power} to {entity.name}'s defense")
          elif self.type=="atk":
               entity.attack = entity.attack+self.power*2
               print(f"added {self.power*2} to {entity.name}'s power")
          else:
               entity.maxHP = entity.maxHP+10
               entity.armor = entity.armor+self.power*0.25
               entity.attack = entity.attack + self.power
               print(f"added 10 max health, {self.power*0.25} defense, and {self.power} attack power to {entity.name}")

