from playable_character import PlayableCharacter
from guild import Guild
import random

class Rogue(PlayableCharacter):

  def __init__(self, name: str, gold: float, guild: Guild):
    super().__init__(name, gold, guild)
    self.attack_power = 100 + guild.attack_bonus

  def is_alive(self):
    return super().is_alive()
  
  def take_coins(self, other: PlayableCharacter, amount: float):
    return super().take_coins(other, amount)
  
  def loot_dead_character(self, other):
    return super().loot_dead_character(other)

  def greet(self, other: PlayableCharacter) -> None:
    if(self.is_alive() and other.gold > 0):
      print("Good day stranger. *You bow your head and slip one of the stranger's coins in your pocket.*")
      self.take_coins(other, 1)

  def drink_health_potion(self):
    if(self.is_alive()):
      return super().drink_health_potion()

  def drink_potion(self) -> None:
    if(self.is_alive()):
      self.drink_health_potion()

  def attack(self, other: PlayableCharacter) -> None:
    if(self.is_alive() and other.is_alive()):
      d20 = random.randint(1, 20)
      if(d20<18):
        print("*Your target avoids your attack and you fall miserably on your face.*")
      else:
        print("*Your dagger stucks just under your opponent's shoulder blades, effectively killing them.*")
        other.health.points = 0
      self.loot_dead_character(other)
  
  def interact_with_npc(self, npc):
    if(self.is_alive()):
      return super().interact_with_npc(npc)