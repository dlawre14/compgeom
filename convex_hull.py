#Convex Hull Algorithms

from my_modules.geom.point import Point
from my_modules.geom.utils import utils as utils

from my_modules.listeners.graphicslistener import GraphicsListener
from my_modules.listeners.delaylistener import DelayListener

from fractions import Fraction
from operator import attrgetter

import argparse

parser = argparse.ArgumentParser(description='Suite of convex hull algorithms with optional graphical implementation')
parser.add_argument ('-p', type=int, help='number of points to generate', required=True)
parser.add_argument ('--seed', type=int, help='seed to use for random point generation')
parser.add_argument ('-algorithm', type=str, help='algorithm to use, available options: monotone', required=True)
parser.add_argument ('-g', action='store_true', default=False, help='add a graphical output to the program')
parser.add_argument ('-v', action='store_true', default=False, help='add a text output to the program')
parser.add_argument ('-d', type=float, default=0, help='add a delay to the program, -1 is for manual advance, > 0 is for a timed delay')

def monotoneChain(points, listeners):
  points = sorted(points, key=attrgetter('_x', '_y'))
  for l in listeners: l.setPointColor(points[0], 'green')

  edgePoints = []
  edgePoints.append(points[0])


  topPoints = [points[0]]
  bottomPoints = []

  for p in points:
    while len(topPoints) >= 2 and utils.pointDirection(topPoints[-2], topPoints[-1], p) <= 0:
      #l.removeLine(topPoints[-2], topPoints[-1])
      topPoints.pop()

    topPoints.append(p)
    #draw calls here

  points.reverse()
  for p in points:
    while len(bottomPoints) >= 2 and utils.pointDirection(bottomPoints[-2], bottomPoints[-1], p) <= 0:
      #l.removeLine(bottomPoints[-2], bottomPoints[-1])
      bottomPoints.pop()

    bottomPoints.append(p)
    #draw calls here

  for p in topPoints:
    for l in listeners:
      l.setPointColor(p, 'red')

  for p in bottomPoints:
    for l in listeners:
      l.setPointColor(p, 'blue')

  edge = topPoints + bottomPoints

  for l in listeners:
    l.drawPolygon(edge)


args = parser.parse_args()

listeners = []

if args.g:
  listeners.append(GraphicsListener())

if args.d != 0:
  listeners.append(DelayListener(args.d))

ps = utils.pointsInCircle(150, args.p, (200,200), args.seed)

for p in ps:
  for l in listeners:
    l.pointAdded(p)

if args.algorithm == 'monotone':
  monotoneChain(ps, listeners)
