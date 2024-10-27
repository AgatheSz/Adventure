class Health:
  def __init__(self, points: int):
    self.points = points
  
  def add_health(self, amount:int):
    self.points += amount

  def subtract_health(self, amount:int):
    self.points -= amount