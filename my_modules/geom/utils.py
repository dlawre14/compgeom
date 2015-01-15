import random

class utils:

  @staticmethod
  def pointsInCircle(radius, numPoints, seed=None):
    '''This returns a random point in the unit circle'''
    rand = random.Random(seed)
    points = []
    for i in range(numPoints):
      points.append((rand.random(), rand.random()))
    return points
