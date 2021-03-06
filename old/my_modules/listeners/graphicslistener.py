from ..listeners.listener import Listener #since our algorithms run from the root
import cs1graphics as cs1

class GraphicsListener(Listener):

  def __init__(self, height=400, width=400):
    self.canv = cs1.Canvas(height,width)
    self.points = []
    #All objects are defined by a single or tuple of points that must be
    #contained in self.points
    self.pointObjects = {}
    self.lineObjects = {}
    self.polyObjects = {} #polygons and bigger paths

  def pointAdded(self, point):
    self.points.append(point)
    self.pointObjects[point] = cs1.Circle(5, point.tocs1Point())
    self.pointObjects[point].setFillColor('black')
    self.pointObjects[point].setDepth(1)
    self.canv.add(self.pointObjects[point])

  def pointRemoved(self, point):
    if point in self.points:
      self.canv.remove(self.pointObjects[point])
      del self.pointObjects[point]
    else:
      raise RuntimeError('Specified point not in active point set')

  def segmentAdded(self, segment):
    self.pointAdded(segment.getP1())
    self.pointAdded(segment.getP2())
    self.drawSegment(segment)

  def setPointColor(self, point, color):
    if point in self.points:
      self.pointObjects[point].setFillColor(color)
      self.pointObjects[point].setDepth(1)
    else:
      raise RuntimeError('Specified points not in active point set')

  def drawLine(self, p1, p2):
    '''This draws a line between any two known points'''
    if p1 in self.points and p2 in self.points:
      self.lineObjects[(p1,p2)] = cs1.Path(p1.tocs1Point(), p2.tocs1Point())
      self.lineObjects[(p1,p2)].setBorderWidth(2)
      self.lineObjects[(p1,p2)].setDepth(1)
      self.canv.add(self.lineObjects[(p1,p2)])

    else:
      raise RuntimeError('Specified points not in active point set')

  def drawSegment(self, segment):
    self.drawLine(segment.getP1(), segment.getP2())

  def drawLineNonSet(self, p1, p2):
    '''Draw a line between any two points, even if unknown in set'''
    self.lineObjects[(p1,p2)] = cs1.Path(p1.tocs1Point(), p2.tocs1Point())
    self.lineObjects[(p1,p2)].setBorderWidth(2)
    self.lineObjects[(p1,p2)].setDepth(1)
    self.canv.add(self.lineObjects[(p1,p2)])

  def drawSegmentNonSet(self, segment, color = 'black'):
      self.drawLineNonSet(segment.getP1(), segment.getP2())
      self.setSegmentColor(segment, color)

  def setLineColor(self, p1, p2, color):
    if p1 in self.points and p2 in self.points:
      self.lineObjects[(p1,p2)].setBorderColor(color)

    else:
      raise RuntimeError('Specified points not in active point set')

  def setSegmentColor(self, segment, color='red'):
      try:
          self.lineObjects[(segment.getP1(), segment.getP2())].setBorderColor(color)
      except:
          raise RuntimeError('Segment not in active set')

  def removeLine(self, p1, p2):
    if p1 in self.points and p2 in self.points:
      self.canv.remove(self.lineObjects[(p1,p2)])
      del self.lineObjects[(p1,p2)]

    else:
      raise RuntimeError('Specified points not in active point set')

  def removeSegment(self, segment):
      try:
          self.canv.remove(self.lineObjects[(segment.getP1(), segment.getP2())])
          del self.lineObjects[(segment.getP1(), segment.getP2())]
      except:
          raise RuntimeError('Segment not in active set')

  def drawPath(self, pointList):
    pointList = tuple(pointList)
    for point in pointList:
      if point not in self.points:
        raise RuntimeError('Specified points not in active point set')
    self.polyObjects[pointList] = cs1.Path([x.tocs1Point() for x in pointList])
    self.polyObjects[pointList].setBorderWidth(2)
    self.polyObjects[pointList].setsetDepth(1)
    self.canv.add(self.polyObjects[pointList])

  def drawPolygon(self, pointList, color='bisque3'):
    pointList = tuple(pointList)
    for point in pointList:
      if point not in self.points:
        raise RuntimeError('Specified points not in active point set')
    self.polyObjects[pointList] = cs1.Polygon([x.tocs1Point() for x in pointList])
    self.polyObjects[pointList].setFillColor(color)
    self.polyObjects[pointList].setDepth(2)
    self.canv.add(self.polyObjects[pointList])
