from queue import Queue

from triangle import Triangle
import modules.Point as Point

class PointFinder:

    class Node:
        def __init__(self, value):
            self._children = []
            self._triangle = value

        def addChild(self, child):
            self._children.append(child)

        def getChildren(self):
            return self._children

        def getTriangle(self):
            return self._triangle

    def __init__(self):
        self._regions = [] #internal
        self._root = None #a node

    def parse(self, target):
        #parses the DAG until target is found
        if self._root is None:
            raise TypeError('Root is null')

        q = Queue()
        q.put(self._root)
        while not q.empty():
            curr = q.get()

            if curr.getTriangle() == target.getTriangle():
                return curr

            for child in curr.getChildren():
                q.put(child)

        raise LookupError('Triangle region not found')

    def addTriangle(self, tri, *parents):
        if self._root is None:
            self._root = self.Node(tri)
            return

        ps = [] #find all parents
        for p in parents:
            ps.append(self.parse(p))
        for p in ps:
            p.addChild(self.Node(tri))

    def findPoint(self, point):
        if self._root is None:
            raise TypeError('Root is null')

        curr = self._root

        while True: #this will be broken by a return

            for c in curr.getChildren():
                if point in c.getTriangle():
                    change = True
                    curr = c

            if curr.getChildren() == []:
                return curr #we found the smallest region we're in


if __name__ == '__main__':
    pass
