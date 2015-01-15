#Convex Hull Algorithms

from my_modules.geom.point import Point
import my_modules.cs1.cs1graphics as cs1
from my_modules.geom.utils import utils as utils

from fractions import Fraction

#todo

rands = utils.pointsInCircle(50,100,(100,100),321)
points = []

for x,y in rands:
  points.append(Point(x,y))

canv = cs1.Canvas()

for p in points:
  canv.add(cs1.Circle(2, cs1.Point(p.getFloatX(), p.getFloatY())))
