from my_modules.listeners.listener import Listener #since our algorithms run from the root
import cs1graphics as cs1

class GraphicsListener(Listener):

  def __init__(self, height=400, width=400):
    self.canv = cs1.Canvas(height,width)
    self.points = []
    self.graphicalPointObjects = {}

  def pointAdded(self, point):
    self.points.append(point)
    self.graphicalPointObjects[point] = cs1.Circle(2, point.tocs1Point())
    self.graphicalPointObjects[point].setFillColor('black')
    self.canv.add(self.graphicalPointObjects[point])
