try:
  from point import Point
except:
  from my_modules.geom.point import Point

try:
  #this is essentially so we can import in when calling at top level
  from my_modules.geom.utils import utils as utils
except:
  raise RuntimeError('The utility module could not be imported in the segment class')

from fractions import Fraction

class Segment:
  '''Define a line segment with endpoints p1 and p2'''
  def __init__(self, p1, p2):
    self._p1 = None
    self._p2 = None
    if p1.getY() < p2.getY():
        self._p1 = p1
        self._p2 = p2
    elif p1.getY() > p2.getY():
        self._p1 = p2
        self._p2 = p1
    else: #the case of a segment that is horizontal
        if p1.getX() >= p2.getX():
            self._p1 = p1
            self._p2 = p2
        else:
            self._p1 = p2
            self._p2 = p1

  def __eq__(self, other):
      return (self._p1 == other._p1) and (self._p2 == other._p2)

  def __str__(self):
    return '{' + str(self._p1) + ' -> ' + str(self._p2) + '}'

  def __repr__(self):
    return '{' + str(self._p1) +  ' -> ' + str(self._p2) + '}'

  def __contains__(self, a):
      if self._p1 == a or self._p2 == a:
          return True
      else:
          return False

  def __hash__(self):
      return hash(self._p1) - hash(self._p2)

  def getP1(self):
    return self._p1

  def getP2(self):
    return self._p2

  def getValueAtX(self, x):
      '''returns the coordinate value of the segment at x'''
      slope = abs(self._p1.getY() - self._p2.getY())/abs(self._p1.getX()-self._p2.getX())
      intercept = self._p1.getY() - (slope * self._p1.getX())
      y = slope * x + intercept
      return Point(x,y)

  def getValueAtY(self, y):
      '''returns the coordinate value of the sement at y'''
      if self._p1.getX()-self._p2.getX() == 0:
          #perturb by epsilon
          slope = abs(self._p1.getY() - self._p2.getY())/abs(self._p1.getX()-self._p2.getX()+Fraction(1,100000000))
      else:
          slope = abs(self._p1.getY() - self._p2.getY())/abs(self._p1.getX()-self._p2.getX())

      intercept = self._p1.getY() - (slope * self._p1.getX())
      x = (intercept - y) / slope
      return Point(x, y)

  def leftOf(self, other, val):
    '''is self left of other at given Y'''
    if self.getValueAtY().getX() <= other.getValueAtY().getX():
      return True
    else:
      return False

  def intersects(self, other):
    '''determines if a segment intersects another'''
    o1 = utils.pointDirection(self._p1, self._p2, other._p1)
    o2 = utils.pointDirection(self._p1, self._p2, other._p2)
    o3 = utils.pointDirection(other._p1, other._p2, self._p1)
    o4 = utils.pointDirection(other._p1, other._p2, self._p2)

    o = [o1,o2,o3,o4]
    o = list(map(utils.directionRound, o))

    if (o[0] != o[1] and o[2] != o[3]):
      return True

    return False
