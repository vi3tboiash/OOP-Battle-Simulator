import random
import math
class Equipment:
     def __init__(self, name, Type):
          self.name = name
          self.type = Type
          #rarity determines how strong a piece of equipment is
          self.rarity = random.randint(0,30)
          #power is a percentage of the rarity of the equipment
          self.power = math.trunc(self.rarity*(random.randint(0,1000)/1000))


     def add(self, entity):
          #adds equipment to your equipment list unless it's a potion
          if self.type != "potion":
               entity.equipAmt += 1
               entity.equipList.append(self)
               print(f"{entity.equipAmt} currently equipped, {entity.equipMax} is the max")
          #if you have too much equipment it asks you to switch one out
          if entity.equipAmt - entity.equipMax > 0:
               for x in range(len(entity.equipList)):
                    print(entity.equipList[x].name)
               ans = input("You have max equipment! would you like to trade one out? (y/n)").lower()
               #switches one out and reduces stats based on what you lost
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
               # doesn't take new equipment
               elif ans == "n":
                    print(f"{self.name} was not equipped")
               #edge case
               else:
                    print("type only \"y\" or only \"n\"")
               #reduces amount of equipment back down
               entity.equipAmt -= 1

          #defining what each equipment type does(if it doesn't have a known equipment type it just does everything)
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
               entity.armor = math.trunc(entity.armor+self.power*0.25)
               entity.attack_power = entity.attack_power + self.power
               print(f"added 10 max health, {math.trunc(self.power*0.25)} defense, and {self.power} attack power to {entity.name}")


