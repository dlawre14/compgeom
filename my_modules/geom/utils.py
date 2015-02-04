import random
import math

#directory issues
try:
  from point import Point
except:
  from my_modules.geom.point import Point

class utils:
  '''This class will only contain static methods'''

  @staticmethod
  def pointsInCircle(radius, numPoints, centerPt=(0,0), seed=None):
    '''This returns a random point in the unit circle'''
    rand = random.Random(seed)
    points = []
    for i in range(numPoints):
      #simple circle generator, we're using trig here and then pretending we didn't
      angle = rand.random() * math.pi * 2
      rad = rand.randrange(radius + 1)
      x = centerPt[0] + int(rad * math.cos(angle))
      y = centerPt[1] + int(rad * math.sin(angle))
      points.append(Point(x,y))

    return points

  def pointsInRectangle(width, height, numPoints, centerPt=Point(0,0), seed=None):
    rand = random.Random(seed)
    points = []
    for i in range(numPoints):
      points.append(Point(rand.randrange(-width//2,width//2+1), rand.randrange(-height//2,height//2+1)) + centerPt)

    return points

  @staticmethod
  def pointDirection (p1,p2,p3):
    '''Checks if three points move clockwise'''
    '''returns < 0 for counterclockwise, > 0 for clockwise, and 0 for co-linear'''
    return ((p2.getX() - p1.getX()) * (p3.getY() - p1.getY())) - ((p2.getY() - p1.getY()) * (p3.getX() - p1.getX()))

  @staticmethod
  def directionRound(num):
    if num > 0:
      return 1
    elif num < 0:
      return -1
    else:
      return 0

  @staticmethod
  def averageCoord (ps):
    '''Take a list of point and averages them'''
    xSum = 0
    ySum = 0
    for p in ps:
      xSum += p.getX()
      ySum += p.getY()

    return Point(xSum/len(ps), ySum/len(ps))

  def polyTangents (p1, p2):
    '''Find tangents between two polygons p1 and p2'''
    '''This returns points defining the upper and lower tangent'''

    #TODO

    return None
