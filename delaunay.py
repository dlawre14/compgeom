import cs1graphics as cs1
cs1Point = cs1.Point
import modules.Point as Point

import modules.DCEL as DCEL
from modules.RandomGeom import RandomGeom
from old.my_modules.listeners.delaylistener import DelayListener
from old.my_modules.listeners.graphicslistener import GraphicsListener

from triangle import Triangle
from pointfinder import PointFinder

from queue import Queue

#for easiness, returns a polygon
def drawTri(triangle):
    tri = cs1.Polygon(map(PointToCS, triangle.getPoints()))
    return tri

def PointToCS(point):
    return cs1Point(point.getX(), point.getY())

def computeDelaunay(points, listeners=[]):
    pass

    return DCEL()

if __name__ == '__main__':
    #Do arg parsing at some point
    #listeners = [GraphicsListener(), DelayListener(0.25)]
    canv = cs1.Canvas(500,500)

    #so we can color things
    tris = {}

    #Create arbitrary bounding triangle
    bounds = [Point.Point2D(250,5), Point.Point2D(10,490), Point.Point2D(490,490)]
    bound = Triangle(bounds[0], bounds[1], bounds[2])

    poly = drawTri(bound)
    canv.add(poly)

    tris[bound] = poly

    event = 1

    points = Queue()
    finder = PointFinder()
    finder.addTriangle(bound)

    while event != None:
        event = canv.wait()
        if event.getDescription() == 'keyboard':
            event = None
        else:
            p = event.getMouseLocation()
            points.put(Point.Point2D(p.getX(), p.getY()))
            canv.add(cs1.Circle(5,p))

    while not points.empty():
        p = points.get()
        region = finder.findPoint(p)
        ps = region.getTriangle().getPoints()

        color = input('Set point region color: ')
        tris[region.getTriangle()].setFillColor(color)

        newtris = []
        for i in range(len(ps)):
            newtris.append(Triangle(ps[i], ps[(i+1) % 3], p))
        for tri in newtris:
            t = drawTri(tri)
            canv.add(t)
            tris[tri] = t
            finder.addTriangle(tri, region)

        input('Press enter to proceed with next point.')

    canv.close()
