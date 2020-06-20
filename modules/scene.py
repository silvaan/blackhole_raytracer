from modules.image import Image

class Scene:
  def __init__(self, camera, blackhole, disk, width, height):
    self.camera = camera
    self.width = width
    self.height = height
    self.image = Image(width, height)
    self.blackhole = blackhole
    self.disk = disk