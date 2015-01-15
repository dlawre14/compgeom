#Convex Hull Algorithms

from my_modules.geom.point import Point
import my_modules.cs1.cs1graphics as cs1
from my_modules.geom.utils import utils as utils

from fractions import Fraction

#todo

rands = utils.pointsInCircle(5,10,321)
points = []

for x,y in rands:
  points.append(Point(x,y))

points.append(Point(Fraction(3,4), Fraction(1,2)))

for p in points:
  print (p)
