from abc import abstractmethod
from character import Character
from npc import Npc
from guild import Guild
from health import Health

class PlayableCharacter(Character):
  def __init__(self, name: str, gold: float, guild: Guild):
    super().__init__(name, gold)
    self.health = Health(100)
    self.attack_power = 0
    self.guild = guild

  @abstractmethod
  def is_alive(self) -> bool:
    if(self.health.points>0):
      return True
    else:
      print(f"{self.name} is dead.")
      return False
    
  @abstractmethod
  def take_coins(self, other, amount: float):
    self.gold += amount
    other.gold -= amount

  @abstractmethod
  def loot_dead_character(self, other):
    if(not other.is_alive()):
      self.take_coins(other, other.gold)
      print(f"*Your opponent is no more, so you decide to loot their gold coins. You now have {self.gold} golds.*")


  @abstractmethod
  def greet(self, other) -> None:
    pass

  @abstractmethod
  def drink_health_potion(self) -> None:
    if(self.health.points <=50):
      print("*You drink a health potion and feel instantly better.*")
      self.health.add_health(50)
    elif(self.health.points < 100):
      print("*You drink a health potion and feel instantly better.*")
      self.health.points = 100

  @abstractmethod
  def drink_potion(self) -> None:
    pass

  @abstractmethod
  def attack(self, other) -> None:
    pass
  
  @abstractmethod
  def interact_with_npc(self, npc:Npc) -> None:
    npc.greet()
    match(npc.type):
      case "seller":
        print("*You start browsing through the items the itinerant sellers has to show you.*")
      case "villager":
        print("Good morrow humble villager. *You exchange some hollow words with the Villager.*")
      case "guard":
        print("*You ask the guard about directions to a place in the city.*")