#from Rational import Rational
from fractions import Fraction as Rational

class Point:
    """Represents a point in an arbitrary dimension using integer or rational coordinates.

    A point is immutable and indexible."""

    def __init__(self, *coords):
        """Construct point from given initial coordiantes.

        coords can be expressed in one of three ways:
          1)  an existing Point instance, which will be cloned
          2)  a single sequence containing all coordinates
          3)  independent parameter sequence, each of which is a coordinate.
        """
        coords = self._prepareCoords(coords)
        self._coords = coords

    def _prepareCoords(self,coords):
        """Creates tuple of coordinates from parameter, which may be tuple,list or existing point"""
        if len(coords) == 1:
            if isinstance(coords[0], (tuple,list)):
                coords = tuple(coords[0])
            elif isinstance(coords[0], Point):
                coords = coords[0]._coords
        return coords

    def _factory(self, coords):
        """Factory function for creating new points."""
        return Point(coords)

    def extend(self, *coords):
        """Construct point by extending with additional coordinates.

        coords can be a series of parameters designating the
        coordinates, or can be a single parameter which is itself a
        sequence of coordinates.
        """
        if len(coords) == 1 and isinstance(coords[0],(tuple,list)):
            newest = self._coords + tuple(coords[0])
        else:
            newest = coords
        return self._factory(self._coords + newest)

    def __len__(self):
        """Returns the dimension of the point."""
        return len(self._coords)

    def __getitem__(self, index):
        """Return the i-th coordinate of point."""
        return self._coords[index]

    def __repr__(self):
        """Return string representation of point using angle brackets."""
        return '<' + ', '.join([str(x) for x in self._coords]) + '>'

    def __neg__(self):
        """Project the point across the origin."""
        coords = [-x for x in self._coords]
        return self._factory(coords)

    def norm(self, p=2):
        """Return floating-point norm of the point.

        If p is None, uses infinity norm.
        """
        if p is None:
            return max([abs(x) for x in self._coords])
        elif isinstance(p,(int)):
            if p>0:
                return self.normPower() ** (1.0 / p)
            else:
                raise ValueError('power must be positive integer')
        else:
            raise TypeError('power must be positive integer')


    def normPower(self, p=2):
        """Return norm of the point before taking the root."""
        if isinstance(p,(int)):
            if p > 0:
                total = 0
                for i in range(len(self._coords)):
                    total += pow(abs(self[i]),p)
                return total
            else:
                raise ValueError('power must be positive integer')
        else:
            raise TypeError('power must be positive integer')


    def withinBall(self, center, radius, p=2):
        """Determine whether point is at or within given radius from center (using specified norm)."""
        d = (center-self).normPower(p)
        return d <= radius ** p

    def _sameDimension(self, other):
        if len(self) != len(other):
            raise ValueError('Points are not expressed with same dimension.')

    def __add__(self, other):
        self._sameDimension(other)
        coords = [self[i] + other[i] for i in range(len(self))]
        return self._factory(coords)

    def __sub__(self, other):
        self._sameDimension(other)
        coords = [self[i] - other[i] for i in range(len(self))]
        return self._factory(coords)

    def __mul__(self, operand):
        if isinstance(operand, (int,float,Rational)):             # multiply by constant
            coords = [c * operand for c in self]
            return self._factory(coords)
        elif isinstance(operand, Point):                          # dot product
            self._sameDimension(operand)
            return sum( [ self[i] * operand[i] for i in range(len(self)) ] )

    def __rmul__(self, operand):
        return self * operand

    def distance(self, other, p=2):
        """Return distance between two points, using given metric."""
        self._sameDimension(other)
        return (self - other).norm(p)

    def __cmp__(self, other):
        """Compare two points according to first dimension.

        Ties are broken lexicographically, when possible.

        ValueError raised if points do not have same dimension.
        """
        if len(self) == len(other):
            return cmp(self._coords, other._coords)
        else:
            raise ValueError('can only compare points with equivalent dimensions.')

#########################################################################################

class Point2D(Point):
    def __init__(self, *coords):
        """Construct point from given initial coordiantes.

        coords can be a series of parameters designating the
        coordinates, or can be a single parameter which is itself a
        sequence of coordinates.
        """
        coords = self._prepareCoords(coords)
        if len(coords) == 2:
            self._coords = coords
        else:
            raise ValueError('Point2D must have precisely two coordinates')

    def getX(self):
        return self[0]

    def getY(self):
        return self[1]

    def rotate90(self):
        """Returns new point rotated 90 degrees clockwise about origin"""
        return Point2D( (-self.y, self.x) )

    def _factory(self, coords):
        """Factory function for creating new points."""
        return Point2D(coords)


#########################################################################################
class Point3D(Point):

    def __init__(self, *coords):
        """Construct point from given initial coordiantes.

        coords can be a series of parameters designating the
        coordinates, or can be a single parameter which is itself a
        sequence of coordinates.
        """
        coords = self._prepareCoords(coords)
        if len(coords) == 3:
            self._coords = coords
        else:
            raise ValueError('Point3D must have precisely two coordinates')

    def getX(self):
        return self[0]

    def getY(self):
        return self[1]

    def getZ(self):
        return self[2]

    def _factory(self, coords):
        """Factory function for creating new points."""
        return Point3D(coords)

    def cross(self, other):
        """Return cross product of two three-dimensional points.

        ValueError if given points are not three-dimensional.
        """
        if isinstance(other, Point3D):
            return self._factory(self[1]*other[2] - self[2]*other[1],
                                 self[2]*other[0] - self[0]*other[2],
                                 self[0]*other[1] - self[1]*other[0])
        else:
            ValueError('Cross product only defined for Point3D class.')

#########################################################################################

class Line:
    """Represents a line in arbitrary dimension."""
    def __init__(self, p, qNone):
        """Point can be initialized in one of two ways.

        p and q can be Point instances, in which case the line is the
        unique one passing through those points (or an undefined line
        if points are the same).

        Alternatively, the line can be specified with Point p
        designating a non-zero vector, and scalar q being the dot
        product achieved between p and all points incident to the
        line.
        """
        if not isinstance(p,Point):
            raise TypeError('p must be a Point instance')
        if isinstance(q,Point):
            if len(p) == len(q):
                coords = [ p[i]-q[i]  for i in range(len(p)) ]
                p = p._factory(coords)
                q = p*q
            else:
                raise ValueError('points must be expressed in same dimension')
        if not isinstance(q,(int,Rational)):
            raise TypeError('q must be a Point or a scalar value')
        self._vector = p
        self._dot = q

    def isUndefined(self):
        return self._vector * self._vector == 0

    def isParallel(self, other):

        return self._a * other._b - self._b * other._a == 0

    def intersection(self,other):
        det = self._a * other._b - self._b * other._a
        x = Rational(other._b * self._c - self._b * other._c, det)
        y = Rational(self._a * other._c - self._c * other._a, det)
        return Point(x,y)


#########################################################################################

def readPointsFromFile(f):
    """Read a sequence of points from a text file, returing the list of Point instances.

    Format is expected as one point per line, with each point having
    coordinates separated by spaces.
    """
    points = []
    for line in f:
        coords = []
        indiv = line.split()
        for i in indiv:
            pieces = i.split('/')
            if len(i) == 1:
                coords += int(pieces[0])
            elif len(i) == 2:
                coords += Rational(pieces[0],pieces[1])
            else:
                raise ValueError('Illegal coordinate expressed: ' + i)
        points += Point(coords)
    return points


#########################################################################################
