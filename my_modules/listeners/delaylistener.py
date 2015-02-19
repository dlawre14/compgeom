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
