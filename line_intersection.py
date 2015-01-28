import argparse

from my_modules.geom.segment import Segment
from my_modules.geom.point import Point

#TODO
s = Segment(Point(3,5), Point(7,10))
print (s.getValueAtX(4))
