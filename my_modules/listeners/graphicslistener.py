from my_modules.listeners.listener import Listener #since our algorithms run from the root
import cs1graphics as cs1

class GraphicsListener(Listener):

  def __init__(self, height=400, width=400):
    self.canv = cs1.Canvas(height,width)
    self.points = []
    self.pointObjects = {}
    self.lineObjects = {}

  def pointAdded(self, point):
    self.points.append(point)
    self.pointObjects[point] = cs1.Circle(5, point.tocs1Point())
    self.pointObjects[point].setFillColor('black')
    self.canv.add(self.pointObjects[point])

  def setPointColor(self, point, color):
    if point in self.points:
      self.pointObjects[point].setFillColor(color)
    else:
      raise RuntimeError('Specified points not in active point set')

  def drawLine(self, p1, p2):
    '''This draws a line between any two known points'''
    if p1 in self.points and p2 in self.points:
      self.lineObjects[(p1,p2)] = cs1.Path(p1.tocs1Point(), p2.tocs1Point())
      self.lineObjects[(p1,p2)].setBorderWidth(2)
      self.canv.add(self.lineObjects[(p1,p2)])

    else:
      raise RuntimeError('Specified points not in active point set')