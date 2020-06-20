import numpy as np

class Vector:
  def __init__(self, x=0, y=0, z=0):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.norm = np.sqrt(self.x**2+self.y**2+self.z**2)
  
  def normalize(self):
    return self / self.norm

  def dot(self, other):
    return self.x*other.x + self.y*other.y + self.z*other.z

  def cross(self, other):
    return Vector(
        self.y*other.z - self.z*other.y,
        self.z*other.x - self.x*other.z,
        self.x*other.y - self.y*other.x
      )
  
  def __str__(self):
    return f'Vector({self.x}, {self.y}, {self.z})'
  
  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
  
  def __sub__(self, other):
    return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
  
  def __mul__(self, other):
    if isinstance(other, Vector):
      return self.dot(other)
    else:
      return Vector(self.x*other, self.y*other, self.z*other)
      
  def __rmul__(self, other):
    return self.__mul__(other)
  
  def __truediv__(self, other):
    return Vector(self.x/other, self.y/other, self.z/other)
  
  def __pow__(self, exp):
    return self*self

  def dist(self, other):
    return (self-other).norm

  def reflect(self, other):
    other = other.normalize()
    return self - 2 * (self * other) * other

  def rotate_x(self, theta):
    theta = theta*np.pi/180
    return Vector(
      self.x,
      np.cos(theta)*self.y-np.sin(theta)*self.z,
      np.sin(theta)*self.y+np.cos(theta)*self.z
    )

  def rotate_z(self, theta):
    theta = theta*np.pi/180
    return Vector(
        np.cos(theta)*self.x-np.sin(theta)*self.y,
        np.sin(theta)*self.x+np.cos(theta)*self.y,
        self.z
      )

Point = Vector