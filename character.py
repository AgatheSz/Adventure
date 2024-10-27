from abc import ABC, abstractmethod

class Character(ABC):
  def __init__(self, name:str, gold:float):
    self.name = name
    self.gold = gold

  @abstractmethod
  def greet(self) -> None:
    pass