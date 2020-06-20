from modules.vector import Point
from modules.color import Color
from modules.blackhole import BlackHole
from modules.disk import Disk
from modules.camera import Camera
from modules.scene import Scene
from modules.engine import Engine

c_origin = Point(0, 0.7, -9.0)
c_focus = Point(0, 0, 0.0)

bh = BlackHole(c_focus, 80)

# You can specify a texture file for the accretion disk with `texture='filename.png'` or a color by `color=Color('#ffffff') (default)`
disk = Disk(c_focus, 4.5*bh.radius, 16.2*bh.radius)

scene = Scene(
	width = 500,
	height = 250,
	camera = Camera(c_origin, c_focus-c_origin, 1.2),
	blackhole = bh,
	disk = disk
)

engine = Engine(scene)
engine.render()

engine.save('images/blackhole.png')