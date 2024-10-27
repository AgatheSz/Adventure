class Rage:
  def __init__(self, points:int):
    self.points = points

  def add_rage(self, amount:int):
    self.points += amount

  def subtract_rage(self, amount:int):
    self.points -= amount