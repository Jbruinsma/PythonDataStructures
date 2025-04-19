class ListNode:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self):
        return f"Val: {self.val}"

    def get_val(self):
        return self.val

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next

    def set_val(self, val):
        self.val = val

    def set_prev(self, prev):
        self.prev = prev

    def set_next(self, next):
        self.next = next
