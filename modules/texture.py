class Texture:
  def __init__(self, im_file, width, height):
    self.pixels = np.array(pil.Image.open(im_file))
    self.width = width
    self.height = height
    self.im_width = self.pixels.shape[0]
    self.im_height = self.pixels.shape[1]

  def get_color(self, x, y):
    x = min(int(round(x*(self.im_width-1)/self.width)), self.im_width-1)
    y = min(int(round(y*(self.im_height-1)/self.height)), self.im_height-1)
    return Color(self.pixels[x, y])