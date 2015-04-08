#This is a specific tree for segments
#This is a binary search tree (not balanced)

class Node:

    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

class segmentTree:

    def __init__(self):
        self.size = 0
        self.root = None
        self.yval = 0 #Note this is segment specific

    def updateY(self, val):
        self.yval = val

    def insert(self, value):
        if self.root == None:
          self.root = Node(value, None)
          self.size += 1
        else:
          self._insert(self.root, value)

    def _insert(self, pos, value):
        if value == pos.value:
            print ('Tree already contains this object')
            return
        if value.getValueAtY(self.yval).leftOf(pos.value.getValueAtY(self.yval)):
            if pos.left is None:
                pos.left = Node(value, pos)
                self.size += 1
            else:
                return self._insert(pos.left, value)
        else:
            if pos.right is None:
                pos.right = Node(value, pos)
                self.size += 1
            else:
                return self._insert(pos.left, value)

    def remove(self, value):
        if self.size < 1:
            raise RuntimeError('Can not remove segment from empty tree.')
        else:
            self._remove(self.root, value)

    def _remove(self, pos, value):
        if value == pos.value:
            if pos.parent == None:
                self.root = None #special case
                size -= 1
                return

            if pos == pos.parent.left:
                pos.parent.left = None
                size -= 1
                return
            else:
                pos.parent.right = None
                size -= 1
                return
        else:
            if value.getValueAtY(self.yval).leftOf(pos.value.getValueAtY(self.yval)):
                if pos.left is None:
                    raise RuntimeError('Value: ' + str(value) + ' is not found.')
                else:
                    return _remove(pos.left, value)
            else:
                if pos.right is None:
                    raise RuntimeError('Value: ' + str(value) + ' is not found.')
                else:
                    return _remove(pos.right, value)
