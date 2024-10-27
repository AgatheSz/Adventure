from character import Character

class Npc(Character):

  def __init__(self, name: str, gold: float, type: str):
    super().__init__(name, gold)
    self.type = type
  
  def greet(self) -> None:
    match(self.type.lower()):
      case "seller":
        print("Good day weary traveller, may I interest in the best quality items ?\n*The seller shows you some rickety old and expensive items.*")
      case "villager":
        print("*The Villager seems busy but takes some precious seconds to politely greet you.*")
      case "guard":
        print("Ah, I used to be an adventurer like you, then I took an arrow to the knee.")