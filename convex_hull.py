#Convex Hull Algorithms

from my_modules.geom.point import Point
from my_modules.geom.utils import utils as utils

from my_modules.listeners.graphicslistener import GraphicsListener

from fractions import Fraction
from operator import attrgetter

l = GraphicsListener()
p = utils.pointsInCircle(175, 25, (200,200))

for point in p:
  l.pointAdded(point)

p = sorted(p, key=attrgetter('_x','_y'))
l.setPointColor(p[0], 'green')
