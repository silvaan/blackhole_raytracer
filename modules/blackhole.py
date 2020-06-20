from modules.constants import G, c

class BlackHole:
  def __init__(self, position, mass):
    self.position = position
    self.mass = mass
    self.radius = 2*self.mass*G/c**2