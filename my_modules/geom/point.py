from fractions import Fraction

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
