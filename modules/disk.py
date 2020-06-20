from modules.color import Color

class Disk:
  def __init__(self, origin, inner_r, outer_r, color=Color('#ffffff'), texture=None):
    self.origin = origin
    self.inner_r = inner_r
    self.outer_r = outer_r
    self.color = color
    if texture is not None:
      self.texture = Texture(texture, 2*self.outer_r, 2*self.outer_r)
    else:
      self.texture = None

  def is_in(self, point):
    r = (point-self.origin).norm
    return r <= self.outer_r and r >= self.inner_r

  def color_at(self, point):
    if self.texture is not None:
      x = point.x
      y = point.z
      return self.texture.get_color(x+self.outer_r, y+self.outer_r)
    else:
      return self.color