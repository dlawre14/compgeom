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
        v0 = self._p2 - self._p1
        v1 = self._p3 - self._p1
        v2 = p - self._p1

        d00 = v0*v0
        d01 = v0*v1
        d11 = v1*v1
        d20 = v2*v0
        d21 = v2*v1
        denom = d00 * d11 - d01 * d01

        v = (d11 * d20 - d01 * d21) / denom
        w = (d00 * d21 - d01 * d20) /denom
        u = 1 - v - w;

        #If on edge, consider inside
        if 0 <= v < 1 and 0 <= w < 1 and 0 <= u < 1:
            return True
        else:
            return False

    def __eq__(self, other):
        if self._p1 == other._p1 and self._p2 == other._p2 and self._p3 == other._p3:
            return True
        else:
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

    #TODO
