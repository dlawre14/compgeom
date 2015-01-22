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
parser.add_argument ('-algorithm', type=str, help='algorithm to use, available options: monotone, jarvis, quick, divide', required=True)
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
    if p.leftOf(leftmost):
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
      if utils.pointDirection(current, best, p) < 0 and p not in edge:
        best = p

      for l in listeners: l.removeLine(current, p)

    edge.append(best)
    print (edge)
    for l in listeners:
      l.setPointColor(best, 'orange')
      l.drawLine(current, best)
    current = best

    if current == leftmost:
      notLooped = False

  for l in listeners:
    l.drawPolygon(edge)

  return edge

def quickHull(points, listeners):

  def solve(ps, a, b):
    if len(ps) < 1:
      return ps

    elif len(ps) < 2:
      for l in listeners:
        try:
          l.removeLine(a,b)
        except:
          pass
        try:
          l.removeLine(b,a)
        except:
          pass

        l.drawLine(a,ps[0])
        l.drawLine(ps[0],b)


    best = ps[0]

    for p in ps:
      if utils.pointDirection(a,b,p) > utils.pointDirection(a,b,best):
        best = p

    for l in listeners:
      try:
        l.removeLine(a,b)
      except:
        pass
      l.drawLine(a,best)
      l.drawLine(b,best)
      l.setPointColor(best, 'orange')

    points = []
    points2 = []

    ps.remove(best)

    for p in ps:
      if utils.pointDirection(a, best, p) >= 0:
        points.append(p)

      if utils.pointDirection(best, b, p) >= 0:
        points2.append(p)

    return solve(points, a, best) + [best] + solve(points2, best, b)


  leftmost = points[0] #arbitrary
  rightmost = points[-1] #arbitrary
  for p in points:
    if p.leftOf(leftmost):
      leftmost = p
    if rightmost.leftOf(p):
      rightmost = p

  for l in listeners:
    l.setPointColor(leftmost, 'green')
    l.setPointColor(rightmost, 'green')
    l.drawLine(leftmost, rightmost)

  points.remove(leftmost)
  points.remove(rightmost)

  leftPoints = []
  rightPoints = []
  for p in points:
    if utils.pointDirection(leftmost, rightmost, p) >= 0:
      for l in listeners: l.setPointColor(p, 'blue')
      leftPoints.append(p)
    else:
      for l in listeners: l.setPointColor(p, 'red')
      rightPoints.append(p)

  edge = [leftmost] + solve(leftPoints, leftmost, rightmost) + [rightmost] + solve(rightPoints, rightmost, leftmost)
  for l in listeners: l.drawPolygon(edge)
  return edge

def divideAndConquer(points, listeners):

  def stitch(p1, p2):
    #stitch together two polygons
    pass

  if len(points <= 3):
    return points

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
elif args.algorithm == 'divide':
  divideAndConquer(ps, listeners)
else:
  raise RuntimeError('You have selected a non-existant algorithm')
