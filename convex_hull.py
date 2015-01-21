#Convex Hull Algorithms

from my_modules.geom.point import Point
from my_modules.geom.utils import utils as utils

from my_modules.listeners.graphicslistener import GraphicsListener
from my_modules.listeners.delaylistener import DelayListener

from fractions import Fraction
from operator import attrgetter

from time import sleep

import argparse

parser = argparse.ArgumentParser(description='Suite of convex hull algorithms with optional graphical implementation')
parser.add_argument ('-p', type=int, help='number of points to generate', required=True)
parser.add_argument ('--seed', type=int, help='seed to use for random point generation')
parser.add_argument ('-algorithm', type=str, help='algorithm to use, available options: monotone, jarvis, quick', required=True)
parser.add_argument ('-g', action='store_true', default=False, help='add a graphical output to the program')
parser.add_argument ('-v', action='store_true', default=False, help='add a text output to the program')
parser.add_argument ('-d', type=float, default=0, help='add a delay to the program, -1 is for manual advance, > 0 is for a timed delay')

def monotoneChain(points, listeners):
  points = sorted(points, key=attrgetter('_x', '_y'))
  for l in listeners: l.setPointColor(points[0], 'green')

  topPoints = []
  bottomPoints = []

  for p in points:
    while len(topPoints) >= 2 and utils.pointDirection(topPoints[-2], topPoints[-1], p) <= 0:
      for l in listeners: l.removeLine(topPoints[-2], topPoints[-1])
      topPoints.pop()

    topPoints.append(p)
    if len(topPoints) > 1:
      for l in listeners: l.drawLine(topPoints[-2], topPoints[-1])

  points.reverse()
  for p in points:
    while len(bottomPoints) >= 2 and utils.pointDirection(bottomPoints[-2], bottomPoints[-1], p) <= 0:
      for l in listeners: l.removeLine(bottomPoints[-2], bottomPoints[-1])
      bottomPoints.pop()

    bottomPoints.append(p)
    if len(bottomPoints) > 1:
      for l in listeners: l.drawLine(bottomPoints[-2], bottomPoints[-1])

  for p in topPoints:
    for l in listeners:
      l.setPointColor(p, 'red')

  for p in bottomPoints:
    for l in listeners:
      l.setPointColor(p, 'blue')

  edge = topPoints + bottomPoints

  for l in listeners:
    l.drawPolygon(edge)

  return edge

def jarvisMarch(points, listeners):
  leftmost = points[0]
  for p in points:
    if p.getX() < leftmost.getX():
      leftmost = p

  for l in listeners:
    l.setPointColor(leftmost, 'red')

  edge = [leftmost]
  current = leftmost
  notLooped = True

  while notLooped: #as long as points remain
    best = points[0]
    for p in points:
      for l in listeners:
        l.drawLine(current, p)
        l.setLineColor(current, p, 'blue')

      #here we're checking directionality
      if utils.pointDirection(current, best, p) < 0:
        best = p

      for l in listeners: l.removeLine(current, p)

    edge.append(best)
    for l in listeners: l.drawLine(current, best)
    current = best

    if current == leftmost:
      notLooped = False

  for l in listeners:
    l.drawPolygon(edge)

  return edge

def quickHull(points, listeners):
  leftmost = points[0]
  rightmost = points[-1]
  for p in points:
    if p.getX() < leftmost.getX():
      leftmost = p
    if p.getX() > rightmost.getX():
      rightmost = p

  for l in listeners:
    l.setPointColor(leftmost, 'green')
    l.setPointColor(rightmost, 'green')
    l.drawLine(leftmost, rightmost)

  furthestUp = points[0]
  furthestDown = points[0]

  for p in points:
    if utils.pointDirection(leftmost, rightmost, p) <= utils.pointDirection(leftmost, rightmost, furthestUp):
      furthestUp = p

    if utils.pointDirection(leftmost, rightmost, p) > utils.pointDirection(leftmost, rightmost, furthestDown):
      furthestDown = p


  for l in listeners:
    l.drawLine(leftmost, furthestUp)
    l.drawLine(rightmost, furthestUp)
    l.setLineColor(leftmost, furthestUp, 'orange')
    l.setLineColor(rightmost, furthestUp, 'orange')

    l.drawLine(leftmost, furthestDown)
    l.drawLine(rightmost, furthestDown)
    l.setLineColor(leftmost, furthestDown, 'cyan')
    l.setLineColor(rightmost, furthestDown, 'cyan')


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
elif args.algorithm == 'jarvis':
  jarvisMarch(ps, listeners)
elif args.algorithm == 'quick':
  quickHull(ps, listeners)
else:
  raise RuntimeError('You have selected a non-existant algorithm')
