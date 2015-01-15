#Convex Hull Algorithms

from my_modules.geom.point import Point
from my_modules.geom.utils import utils as utils

from my_modules.listeners.graphicslistener import GraphicsListener

from fractions import Fraction

l = GraphicsListener()
p = utils.pointsInCircle(175, 500, (200,200), 5)

for point in p:
  l.pointAdded(point)
