#This class exists solely as an interface
#it will be expanded and inherited from to ensure
#consistent listeners

class Listener:

  def __init__(self):
    pass

  def addDelay(self):
    pass

  def drawLineNonSet(self, p1, p2):
    pass

  def pointRemoved(self, point):
    pass

  def drawSegment(self, segment):
    pass

  def segmentAdded(self, segment):
    pass
