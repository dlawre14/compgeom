try:
  #this is essentially so we can import in when calling at top level
  from my_modules.geom.utils import utils as utils
except:
  raise RuntimeError('The utility module could not be imported in the conexpolygon class')


class ConvexPolygon:
    #this could theoretically be a subclass but it's fine like this

    def __init__(self, points):
        '''points is a list of points defining the outer edge'''
        self._points = tuple(points)

    def __getitem__(self, i):
        return self._points[i % (len(self._points)-1)]

    def merge(self, other, listeners = []):
        edge = []

        while True:
            a = 0
            b = 0
            print ("looping")
            while utils.ccw(self._points[a], other._points[b], other._points[b+1]) != utils.ccw(self._points[a], other._points[b], other._points[b-1]):
                a+=1
                print (a)
            while utils.ccw(other._points[b], self._points[a], self._points[a+1]) != utils.ccw(other._points[b], self._points[a], self._points[a-1]):
                b+=1
                print(b)
            if utils.ccw(self._points[a], other._points[b], other._points[b+1]) == utils.ccw(self._points[a], other._points[b], other._points[b-1]) and utils.ccw(other._points[b], self._points[a], self._points[a+1]) == utils.ccw(other._points[b], self._points[a], self._points[a-1]):
                for l in listeners:
                    l.drawLine(self._points[a], other._points[b])
                    l.setPointColor(self._points[a], "yellow")
                    l.setPointColor(other._points[b], "yellow")
                break;



        return ConvexPolygon(edge)
