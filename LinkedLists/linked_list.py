from LinkedLists.ListNode import ListNode


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if not self.is_empty():
            ll_str = ""
            curr = self.head
            while curr:
                ll_str += str(curr.val) + " "
                curr = curr.next
                if curr:
                    ll_str += "<--> "
            return ll_str
        return "Empty list"

    def __len__(self):
        return self.size

    def prepend(self, val):
        if self.is_empty():
            new_node = ListNode(val)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = ListNode(val)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def append(self, val):
        if self.is_empty():
            new_node = ListNode(val)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = ListNode(val)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove(self, val=None, index=None):
        if index is not None:
            if self._check_index(index):
                if index == 0 and self.size > 1:
                    self.head = self.head.next
                    if self.head:
                        self.head.prev = None
                elif index == 0 and self.size == 1:
                    self.head = None
                    self.tail = None
                elif index == self.size - 1:
                    self.tail = self.tail.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    curr_node = self._iterate(index)
                    curr_node.prev.next = curr_node.next
                    if curr_node.next:
                        curr_node.next.prev = curr_node.prev
                self.size -= 1
        elif val is not None:
            curr = self.head
            while curr:
                if curr.val == val:
                    if curr == self.head:
                        self.head = curr.next
                        if self.head:
                            self.head.prev = None
                    elif curr == self.tail:
                        self.tail = curr.prev
                        if self.tail:
                            self.tail.next = None
                    else:
                        curr.prev.next = curr.next
                        if curr.next:
                            curr.next.prev = curr.prev
                    self.size -= 1
                    return
                curr = curr.next

    def contains(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False

    def find(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                return curr
            curr = curr.next

    def _iterate(self, index):
        if self._check_index(index):
            curr = self.head
            count = 0
            while count < index:
                curr = curr.next
                count += 1
            return curr

    def is_empty(self):
        return self.size == 0

    def _check_index(self, index):
        if not index < 0 and not index >= self.size:
            return True
        else:
            return False

def main():
    ll = LinkedList()

    print("Initial list (should be empty):")
    print(ll)
    print("Is empty?", ll.is_empty())
    print("Length:", len(ll))
    print()

    # Append values
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("After appending 10, 20, 30:")
    print(ll)
    print("Length:", len(ll))
    print()

    # Prepend values
    ll.prepend(5)
    ll.prepend(2)
    print("After prepending 5, 2:")
    print(ll)
    print("Length:", len(ll))
    print()

    # Remove by index
    ll.remove(index=0)  # remove 2
    print("After removing index 0 (should remove 2):")
    print(ll)

    ll.remove(index=2)  # remove 30
    print("After removing index 2 (should remove 20):")
    print(ll)
    print()

    # Remove by value
    ll.remove(val=10)
    print("After removing value 10:")
    print(ll)
    print()

    # Check contains
    print("Contains 20?", ll.contains(20))
    print("Contains 5?", ll.contains(5))
    print()

    # Find value
    node = ll.find(5)
    if node:
        print(f"Found node: {node}")
    else:
        print("Value not found")
    print()

    # Final state
    print("Final list:")
    print(ll)
    print("Length:", len(ll))


if __name__ == "__main__":
    main()