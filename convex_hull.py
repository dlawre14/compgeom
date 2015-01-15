#Convex Hull Algorithms

from my_modules.geom.point import Point
from my_modules.geom.utils import utils as utils

from my_modules.listeners.graphicslistener import GraphicsListener

from fractions import Fraction
from operator import attrgetter

import argparse

parser = argparse.ArgumentParser(description='Suite of convex hull algorithms with optional graphical implementation')
parser.add_argument ('-p', type=int, nargs=1, help='number of points to generate')
parser.add_argument ('--seed', type=int, nargs=1, help='seed to use for random point generation')

args = parser.parse_args()

l = GraphicsListener()
ps = utils.pointsInCircle(150, 50, (200,200))
for p in ps:
  l.pointAdded(p)
l.drawPath(ps)
