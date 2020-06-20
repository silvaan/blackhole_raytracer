from modules.constants import G, c
from modules.vector import Vector

class Ray:
  def __init__(self, origin, direction):
    self.origin = origin
    self.position = origin
    self.direction = direction.normalize()
    self.velocity = c*self.direction
    self.acceleration = Vector()
    self.total_time = 0
    self.crossed_xz = False

  def point(self, dist):
    return self.origin + dist*self.direction

  def accelerate(self, a):
    self.acceleration = a

  def step(self, t):
    self.prev_pos = self.position
    self.velocity += self.acceleration*t
    self.velocity = c*self.velocity.normalize()
    self.position += self.velocity*t + (self.acceleration/2)*t**2
    self.total_time += t
    
    self.crossed_xz = 0 <= max(self.prev_pos.y, self.position.y) and 0 >= min(self.prev_pos.y, self.position.y)
    if self.crossed_xz:
      a = self.prev_pos
      b = self.position
      l = b-a
      self.cross_point = Vector(a.x-(a.y/l.y)*l.x, 0, a.z-(a.y/l.y)*l.z)