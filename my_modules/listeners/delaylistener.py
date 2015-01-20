from my_modules.listeners.listener import Listener #since our algorithms run from the root
import cs1graphics as cs1
from time import sleep

class DelayListener(Listener):

  def __init__(self, delayAmt):
    self.delay = delayAmt

  def addDelay(self):
    if self.delay < 0:
      input()
    else:
      sleep(self.delay)

  def pointAdded(self, point):
    pass

  def drawLine(self, p1, p2):
    if self.delay < 0:
      input()
    else:
      sleep(self.delay)

  def removeLine(self, p1, p2):
    if self.delay < 0:
      input()
    else:
      sleep(self.delay)

  def setPointColor(self, point, color):
    if self.delay < 0:
      input()
    else:
      sleep(self.delay)

  def setLineColor(self, p1, p2, color):
    pass

  def drawPolygon (self, pointList):
    pass
