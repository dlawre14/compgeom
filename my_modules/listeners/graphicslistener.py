from my_modules.listeners.listener import Listener #since our algorithms run from the root
import cs1graphics as cs1

class GraphicsListener(Listener):

  def __init__(self, height=400, width=400):
    self.canv = cs1.Canvas(height,width)
