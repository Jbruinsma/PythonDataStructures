class HeapNode:

    def __init__(self, val, parent=None):
        self.parent = parent
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.left is None and self.right is None:
            self.left = HeapNode(val, self)
            return self.left
        elif self.left is not None and self.right is None:
            self.right = HeapNode(val, self)
            return self.right
        elif self.left is not None and self.right is not None:
            return self.left.insert(val)

    def bubble_up(self):
        while self.parent and self.val < self.parent.val:
            self._swap_vals(self, self.parent)
            self = self.parent

    @staticmethod
    def _swap_vals(node1, node2):
        node1.val, node2.val = node2.val, node1.val