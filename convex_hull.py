#Convex Hull Algorithms

from my_modules.geom.point import Point
from my_modules.geom.utils import utils as utils

from my_modules.listeners.graphicslistener import GraphicsListener

from fractions import Fraction
from operator import attrgetter

l = GraphicsListener()
p = utils.pointsInCircle(175, 3, (200,200))

for point in p:
  l.pointAdded(point)

l.setPointColor(p[0], 'red')
l.setPointColor(p[1], 'green')
l.setPointColor(p[2], 'blue')

l.drawLine(p[0], p[1])
l.drawLine(p[1], p[2])

print (utils.pointDirection(p[0], p[1], p[2]))
