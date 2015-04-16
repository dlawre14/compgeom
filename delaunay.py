import cs1graphics as cs1
cs1Point = cs1.Point
import modules.Point as Point

import modules.DCEL as DCEL
from modules.RandomGeom import RandomGeom
from old.my_modules.listeners.delaylistener import DelayListener
from old.my_modules.listeners.graphicslistener import GraphicsListener

class Triangle:

    def __init__(self, p1, p2, p3):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3

    def getPoints(self):
        #return a tuple of the points defining the triangle
        return (self._p1, self._p2, self._p3)

    def pointInside(self, p):
        #Checks if p is in or on the triangle
        return False

def computeDelaunay(points, listeners=[]):
    pass

    return DCEL()

if __name__ == '__main__':
    #Do arg parsing at some point
    #listeners = [GraphicsListener(), DelayListener(0.25)]
    canv = cs1.Canvas()

    generator = RandomGeom(87)
    pts = generator.randPointSetInBall(10, Point.Point2D(100,100), 50)
    print (pts)

    dc = DCEL.buildSimplePolygon(pts)
    temp = DCEL.renderDCEL(dc)
    temp[0].moveTo(0,200)
    canv.add(temp[0])
