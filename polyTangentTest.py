#Testing polygon tangent algorithm
from my_modules.geom.point import Point
from my_modules.geom.utils import utils as utils

from my_modules.listeners.graphicslistener import GraphicsListener
from my_modules.listeners.delaylistener import DelayListener

import convex_hull

#define a left and right pointset
listeners = [GraphicsListener()]

leftSet = utils.pointsInCircle(80, 25, (100,200))
rightSet = utils.pointsInCircle(80, 25, (300,200))

for p in leftSet + rightSet:
  for l in listeners: l.pointAdded(p)

#So we can see the seperate polygons
leftPoly = convex_hull.quickHull(leftSet, listeners)
rightPoly = convex_hull.quickHull(rightSet, listeners)
