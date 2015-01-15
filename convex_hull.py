#Convex Hull Algorithms

from my_modules.geom.point import Point
from my_modules.geom.utils import utils as utils

from my_modules.listeners.graphicslistener import GraphicsListener

from fractions import Fraction
from operator import attrgetter

import argparse

parser = argparse.ArgumentParser(description='Suite of convex hull algorithms with optional graphical implementation')
parser.add_argument ('-p', type=int, help='number of points to generate', required=True)
parser.add_argument ('--seed', type=int, help='seed to use for random point generation')
parser.add_argument ('-algorithm', type=str, help='algorithm to use, available options: monotone', required=True)
parser.add_argument ('-g', action='store_true', default=False, help='add a graphical output to the program')
parser.add_argument ('-v', action='store_true', default=False, help='add a text output to the program')
parser.add_argument ('-d', type=float, help='add a delay to the program, -1 is for manual advance, > 0 is for a timed delay')

args = parser.parse_args()

print (args)

l = GraphicsListener()
ps = utils.pointsInCircle(150, args.p, (200,200))
