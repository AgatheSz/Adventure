from playable_character import PlayableCharacter
from mana import Mana
from guild import Guild
import random

class Wizard(PlayableCharacter):

  def __init__(self, name: str, gold: float, guild: Guild):
    super().__init__(name, gold, guild)
    self.attack_power = 50 + guild.attack_bonus
    self.mana = Mana(50)

  def is_alive(self):
    return super().is_alive()
  
  def take_coins(self, other, amount):
    return super().take_coins(other, amount)
  
  def loot_dead_character(self, other):
    return super().loot_dead_character(other)

  def greet(self) -> None:
    if(self.is_alive()):
      print("Greetings my young friend.")

  def drink_health_potion(self):
    if(self.is_alive()):
      return super().drink_health_potion()

  def drink_potion(self) -> None:
    if(self.is_alive()):
      potion_choice = input("Please choose the type of potion you wish to drink (health or mana):\n")
      match(potion_choice):
        case "mana":
          if(self.mana.points == 0):
            print("*You feebly drink the mana potion. You instantly feel lighter and magic flow through your veins.*")
            self.mana.add_mana(50)
        case "health":
          self.drink_health_potion()
        case _:
          print("*You do not own this kind of potion but I suggest you go to a potions master with your extremely innovative idea. I'm sure they'd love that.*")

  def attack(self, other: PlayableCharacter) -> None:
    if(self.is_alive() and self.mana.points > 0 and other.is_alive()):
      d20 = random.randint(1, 20)
      self.mana.subtract_mana(50)
      if(d20<10):
        print("*All your decades of training couldn't prepare you for this spell to miss so miserably.*")
      else:
        print("*You cast a very powerful spell, greatly weakening your opponent.*")
        other.health.subtract_health(self.attack_power)
        self.loot_dead_character(other)
  
  def interact_with_npc(self, npc):
    if(self.is_alive()):
      return super().interact_with_npc(npc)