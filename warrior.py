from playable_character import PlayableCharacter
from rage import Rage
from guild import Guild
import random

class Warrior(PlayableCharacter):

  def __init__(self, name: str, gold: float, guild: Guild):
    super().__init__(name, gold, guild)
    self.attack_power = 30 + guild.attack_bonus
    self.rage = Rage(50)

  def is_alive(self):
    return super().is_alive()
  
  def take_coins(self, other, amount):
    return super().take_coins(other, amount)
  
  def loot_dead_character(self, other):
    return super().loot_dead_character(other)

  def greet(self) -> None:
    if(self.is_alive()):
      print("Hello, do you need a blade?")

  def drink_health_potion(self):
    if(self.is_alive()):
      return super().drink_health_potion()

  def drink_potion(self) -> None:
    if(self.is_alive()):
      potion_choice = input("Please choose the type of potion you wish to drink (health or rage):\n")
      match(potion_choice):
        case "rage":
          if(self.rage.points == 0):
            print("*You feebly drink the rage potion. You feel your blood boil and power come back to you.*")
            self.rage.add_rage(50)
        case "health":
          self.drink_health_potion()
        case _:
          print("*You do not own this kind of potion but I suggest you go to a potions master with your extremely innovative idea. I'm sure they'd love that.*")

  def attack(self, other: PlayableCharacter) -> None:
    if(self.is_alive() and self.rage.points > 0 and other.is_alive()):
      d20 = random.randint(1, 20)
      self.rage.subtract_rage(25)
      if(d20<8):
        print("*Because of your bad grip, your sword slides between your fingers and falls on the ground with a clang.*")
      else:
        print("*You strike a powerful blow.*")
        other.health.subtract_health(self.attack_power)
        self.loot_dead_character(other)
  
  def interact_with_npc(self, npc):
    if(self.is_alive()):
      return super().interact_with_npc(npc)