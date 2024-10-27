class Mana:
  def __init__(self, points:int):
    self.points = points

  def add_mana(self, amount:int):
    self.points += amount

  def subtract_mana(self, amount:int):
    self.points -= amount