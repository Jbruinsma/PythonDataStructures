class TreeNode:

    def __init__(self, val):
        if val is not None:
            self.val = val
            self.left = None
            self.right = None

    def __str__(self):
        return str(self.val)

    def insert(self, val):
        if val is not None:
            if val < self.val:
                if self.left is None: self.left = TreeNode(val)
                else : self.left.insert(val)
            elif val > self.val:
                if self.right is None: self.right = TreeNode(val)
                else : self.right.insert(val)

    def delete(self, val):
        if val is None: return self
        if val < self.val:
            if self.left is not None: self.left = self.left.delete(val)
        elif val > self.val:
            if self.right is not None: self.right = self.right.delete(val)
        else:   
            if self.left is None and self.right is None: return None
            if self.left is None: return self.right
            if self.right is None: return self.left
            self.val = self.right.min_val()
            self.right = self.right.delete(self.val)
        return self

    def contains(self, val):
        if val is None: return False
        if val == self.val: return True
        elif val < self.val and self.left: return self.left.contains(val)
        elif val > self.val and self.right: return self.right.contains(val)
        return False

    def find(self, val):
        if val is None: return None
        if val == self.val: return self
        if val < self.val and self.left: return self.left.find(val)
        if val > self.val and self.right: return self.right.find(val)
        return None

    def pre_order(self):
        vals = [self.val]
        if self.left: vals += self.left.pre_order()
        if self.right: vals += self.right.pre_order()
        return vals

    def in_order(self):
        vals = []
        if self.left: vals += self.left.in_order()
        vals.append(self.val)
        if self.right: vals += self.right.in_order()
        return vals

    def post_order(self):
        vals = []
        if self.left: vals += self.left.post_order()
        if self.right: vals += self.right.post_order()
        vals.append(self.val)
        return vals

    def level_order(self):
        from collections import deque
        queue = deque([self])
        vals = []
        while queue:
            curr_node = queue.popleft()
            vals.append(curr_node.val)
            if curr_node.left: queue.append(curr_node.left)
            if curr_node.right: queue.append(curr_node.right)
        return vals

    def min_val(self):
        curr = self
        while curr.left: curr = curr.left
        return curr.val

    def max_val(self):
        curr = self
        while curr.right: curr = curr.right
        return curr.val

    def height(self):
        left_height = self.left.height() if self.left else -1
        right_height = self.right.height() if self.right else -1
        return 1 + max(left_height, right_height)

    def size(self):
        left_size = self.left.size() if self.left else 0
        right_size = self.right.size() if self.right else 0
        return 1 + left_size + right_size
