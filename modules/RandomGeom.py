import random
from .Point import Point

class RandomGeom(random.Random):
    """Extension of standard Random class with additional methods for creating geometric input."""

    def randPointInRect(self,*intervals):
        """Create a Point in specified axis-aligned rectangle with coordinates from uniform distribution.

        parameters should be a sequence of (low,high) tuples designating the desired range for each individual dimension.
        """
        if len(intervals) == 1 and isinstance(intervals[0],(tuple,list)):
            intervals = tuple(intervals[0])

        coords = []
        for i in intervals:
            if isinstance(i,tuple) and len(i)==2 and isinstance(i[0],(int)) and isinstance(i[1],(int)):
                coords.append(self.randint(i[0],i[1]))
            else:
                raise TypeError('interval should be (low,high) tuple with integral low,high')
        return Point(coords)

    def randPointSetInRect(self, n, *intervals):
        """Create set of n Points in specified axis-aligned rectangle with coordinates from uniform distribution.

        parameters should be a sequence of (low,high) tuples designating the desired range for each individual dimension.
        """
        points = []
        while len(points) < n:
            pt = randPointInRect(intervals)
            if pt not in points:    # avoid duplicates
                points.append(pt)
        return points


    def randPointInBall(self, center, radius):
        """Create a point within ball of given integral radius around center."""
        # this approach will be inefficient for high dimensions
        boundingBox = [(x-radius,x+radius) for x in center]
        valid = False
        while not valid:
            pt = self.randPointInRect(boundingBox)
            if pt.withinBall(center, radius):
                valid = True
        return pt


    def randPointSetInBall(self, n, center, radius):
        """Create set of n Points within ball of given integral radius around center."""
        points = []
        while len(points) < n:
            pt = self.randPointInBall(center,radius)
            if pt not in points:    # avoid duplicates
                points.append(pt)
        return points


if __name__ == '__main__':
    g = GeomRandom()
