#This is the code for triangulating polygons

from other_modules import RedBlackTree as rbtree
from my_modules.listeners.graphicslistener import GraphicsListener
from my_modules.listeners.delaylistener import DelayListener
from my_modules.geom.utils import utils
from my_modules.geom.point import Point
from my_modules.geom.segment import Segment

from operator import attrgetter

import convex_hull


import argparse

def segComp(a, b):
    global yval

    print ('----')
    print ('\tx value of ' + str(a) + ' is ' + str(a.getValueAtY(yval).getX()))
    print ('\tx value of ' + str(b) + ' is ' + str(b.getValueAtY(yval).getX()))
    print ('----')

    if a.getValueAtY(yval).getX() == b.getValueAtY(yval).getX():
        return 0
    elif a.getValueAtY(yval).getX() < b.getValueAtY(yval).getX():
        return -1
    else:
        return 1

def makeMonotone(segments, listeners=[]):
    global yval
    yval = 0

    sweepline = rbtree.RedBlackTree(segComp)

    #gets all points in order
    points = []
    for s in segments:
        if s.getP1() not in points:
            points.append(s.getP1())
        if s.getP2() not in points:
            points.append(s.getP2())

    points = sorted(points, key=attrgetter('_y', '_x'))
    segments = sorted(segments, key=attrgetter('_p1','_p2'))

    helpers = {} #this is a dictionary keyed by segments and holding a tuple of (point, ismerge)
    edges = [] #the set of all start edges and added diagonals

    for l in listeners:
        l.drawSegmentNonSet(Segment(Point(0,yval), Point(400,yval)))
        l.setSegmentColor(Segment(Point(0,yval), Point(400,yval)))

    for p in points:
        for l in listeners: l.removeSegment(Segment(Point(0,yval), Point(400, yval)))
        yval = p.getY()

        for l in listeners:
            l.drawSegmentNonSet(Segment(Point(0,yval), Point(400,yval)))
            l.setSegmentColor(Segment(Point(0,yval), Point(400,yval)))
            l.addDelay()


        for s in segments:
            if p == s.getP1():
                print ('Inserting: ' + str(s) + ', current point: ' + str(p))
                sweepline.insert(s,s)
            if p == s.getP2():
                print ('Removing: ' + str(s) + ', current point: ' + str(p))
                sweepline.remove(s)
                for l in listeners: l.setSegmentColor(s, 'orange')



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Polygon triangulation with optional graphical implementation')
    parser.add_argument ('-s', type=int, help='number of segments to generate', required=True)
    parser.add_argument ('--seed', type=int, help='seed to use for random point generation')
    parser.add_argument ('-g', action='store_true', default=False, help='add a graphical output to the program')
    parser.add_argument ('-v', action='store_true', default=False, help='add a text output to the program')
    parser.add_argument ('-d', type=float, default=0, help='add a delay to the program, -1 is for manual advance, > 0 is for a timed delay')

    args = parser.parse_args()

    ps = utils.convexPolygon(100, args.s, (200,200), args.seed)

    listeners = []

    if args.g:
        listeners.append(GraphicsListener())
    if args.d != 0:
      listeners.append(DelayListener(args.d))

    segments = []

    for i in range(len(ps) + 1):
        segments.append(Segment(ps[i % len(ps)], ps[(i+1) % len(ps)]))
        for l in listeners: l.segmentAdded(segments[-1])

    makeMonotone(segments, listeners)
