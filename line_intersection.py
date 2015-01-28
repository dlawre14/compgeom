import argparse

from my_modules.geom.segment import Segment
from my_modules.geom.point import Point

from my_modules.listeners.graphicslistener import GraphicsListener

#TODO
s = Segment(Point(100,150), Point(100,200))
s2 = Segment(Point(200,300), Point(180, 150))

l = GraphicsListener()
l.segmentAdded(s)
l.segmentAdded(s2)
l.drawSegment(s)
l.drawSegment(s2)
