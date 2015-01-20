from fractions import Fraction
import cs1graphics as cs1

class Point:

  def __init__(self, x = 0, y = 0):

    #To ensure all numbers are fractional
    if not isinstance(x, Fraction):
      self._x = Fraction(x, 1)
    else:
      self._x = x

    #To ensure all numbers are fractional
    if not isinstance(y, Fraction):
      self._y = Fraction(y, 1)
    else:
      self._y = y

  def getX(self):
    return self._x

  def getY(self):
    return self._y

  def getFloatX(self):
    '''This should not be used for math operations, only for graphical libraries requiring floating point numbers'''
    return float(self._x)

  def getFloatY(self):
    '''This should not be used for math operations, only for graphical libraries requiring floating point numbers'''
    return float(self._y)

  def tocs1Point(self):
    '''Used to make a cs1graphics point quickly'''
    return cs1.Point(self.getFloatX(), self.getFloatY())

  def __hash__(self):
    return hash(self._x) + hash(self._y)

  def __str__(self):
    return '<' + (str(self._x) + ',' + str(self._y)) + '>'

  def __add__(self, other):
    return Point(self._x + other._x, self._y + other._y)

  def __sub__(self, other):
    return Point(self._x - other._x, self._y - other._y)

  def __mul__(self, other):
    return Point(self._x * other._x, self._y * other._y)

  def __div__ (self, other):
    return Point (self._x / other._x, self._y / other._y)

  def dotProduct(self, other): #might wish to ignore
    return (self._x * other._x) + (self._y * other._y)
