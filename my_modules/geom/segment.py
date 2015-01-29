try:
  from point import Point
except:
  from my_modules.geom.point import Point

try:
  #this is essentially so we can import in when calling at top level
  from my_modules.geom.utils import utils as utils
except:
  raise RuntimeError('The utility module could not be imported in the segment class')

class Segment:
  '''Define a line segment with endpoints p1 and p2'''
  def __init__(self, p1, p2):
    self._p1 = p1
    self._p2 = p2

  def getP1(self):
    return self._p1

  def getP2(self):
    return self._p2

  def getValueAtX(self, x):
    '''returns the coordinate value of the segment at x'''
    if x < min(self._p1.getX(), self._p2.getX()) or x > max(self._p1.getX(), self._p2.getX()):
      raise ValueError('This x value is not on the line segment')
    else:
      slope = abs(self._p1.getY() - self._p2.getY())/abs(self._p1.getX()-self._p2.getX())
      intercept = self._p1.getY() - (slope * self._p1.getX())
      y = slope * x + intercept
      return Point(x,y)

  def getValueAtY(self, y):
    '''returns the coordinate value of the sement at y'''
    if y < min(self._p1.getY(), self._p2.getY()) or y > max(self._p1.getY(), self._p2.getY()):
      raise ValueError('This y value is not on the segment')
    else:
      slope = abs(self._p1.getY() - self._p2.getY())/abs(self._p1.getX()-self._p2.getX())
      intercept = self._p1.getY() - (slope * self._p1.getX())
      x = (intercept - y) / slope
      return Point(x, y)

  def intersects(self, other):
    '''determines if a segment intersects another'''
    o1 = utils.pointDirection(self._p1, self._p2, other._p1)
    o2 = utils.pointDirection(self._p1, self._p2, other._p2)
    o3 = utils.pointDirection(other._p1, other._p2, self._p1)
    o4 = utils.pointDirection(other._p1, other._p2, self._p2)

    o = [o1,o2,o3,o4]
    print (o)
    o = list(map(utils.directionRound, o))
    print (o)

    if (o[0] != o[1] and o[2] != o[3]):
      return True

    return False
