class Equipment:
     def __init__(self, name, Type, power):
          self.name = name
          self.type = Type
          self.power = power

     def add(self, entity):
          if self.type != "potion":
               entity.equipAmt += 1
               entity.equipList.append(self)
               print(f"{entity.equipAmt} currently equipped, {entity.equipMax} is the max")
          print("value!!! "+str(entity.equipAmt-entity.equipMax))
          if entity.equipAmt - entity.equipMax > 0:
               for x in range(len(entity.equipList)):
                    print(entity.equipList[x].name)
               ans = input("You have max equipment! would you like to trade one out? (y/n)").lower()
               if ans == "y":
                    slot = int(input("which slot would you like to switch out?"))-1
                    removed = entity.equipList[slot]
                    entity.equipList[slot]=self
                    if removed.type=="armor":
                         entity.armor = entity.armor-int(removed.power)
                    elif removed.type=="atk":
                         entity.attack_power -= removed.power*2
                    else:
                         entity.maxHP = entity.maxHP-10
                         entity.armor = entity.armor-removed.power*0.25
                         entity.attack_power = entity.attack_power - removed.power
               elif ans == "n":
                    print("cool")
               else:
                    print("type only y or only n")


          if self.type=="potion":
               print(f"added {self.power*5} to {entity.name}'s health")
          elif self.type=="def":
               entity.armor = entity.armor + self.power
               print(f"added {self.power} to {entity.name}'s defense")
          elif self.type=="atk":
               entity.attack_power = entity.attack_power+self.power*2
               print(f"added {self.power*2} to {entity.name}'s power")
          else:
               entity.maxHP = entity.maxHP+10
               entity.armor = entity.armor+self.power*0.25
               entity.attack_power = entity.attack_power + self.power
               print(f"added 10 max health, {self.power*0.25} defense, and {self.power} attack power to {entity.name}")

