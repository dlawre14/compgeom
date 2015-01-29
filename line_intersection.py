import argparse

from my_modules.geom.segment import Segment
from my_modules.geom.point import Point

from my_modules.listeners.graphicslistener import GraphicsListener
from my_modules.geom.utils import utils as utils
from my_modules.RedBlackTree import RedBlackTree

ps = utils.pointsInRectangle(100,100, 4, Point(200,200))
l = GraphicsListener()

segments = []
for p in range(2, len(ps) + 1, 2):
  print (p)
  segments.append(Segment(ps[p-1],ps[p-2]))
  l.segmentAdded(segments[-1])
  l.drawSegment(segments[-1])

print (segments[0].intersects(segments[1]))
