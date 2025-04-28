from typing import Any

from LinkedLists.list_node import ListNode


class LinkedList:

    def __init__(self) -> None:
        self.head : ListNode | None = None
        self.tail : ListNode | None = None
        self.size : int = 0

    def __str__(self) -> str:
        if not self.is_empty():
            ll_str : str = ""
            curr : ListNode | None = self.head
            while curr:
                ll_str += str(curr.val) + " "
                curr = curr.next
                if curr:
                    ll_str += " <--> "
            return ll_str
        return " "

    def __len__(self) -> int:
        return self.size

    def prepend(self, val: Any) -> None:
        new_node: ListNode = ListNode(val)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def append(self, val : Any) -> None:
        new_node : ListNode = ListNode(val)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove(self, val : Any =None, index : int =None):
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
                    curr_node : ListNode = self._iterate(index)
                    curr_node.prev.next = curr_node.next
                    if curr_node.next:
                        curr_node.next.prev = curr_node.prev
                self.size -= 1
        elif val is not None:
            curr : ListNode | None = self.head
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

    def contains(self, val: Any) -> bool:
        curr : ListNode | None = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False

    def find(self, val: Any) -> ListNode | None:
        curr : ListNode | None = self.head
        while curr:
            if curr.val == val:
                return curr
            curr = curr.next
        return None

    def _iterate(self, index: int) -> ListNode | None:
        if self._check_index(index):
            curr : ListNode | None = self.head
            count : int = 0
            while count < index:
                curr = curr.next
                count += 1
            return curr
        return None

    def is_empty(self) -> bool:
        return self.size == 0

    def _check_index(self, index : int) -> bool:
        return not index < 0 and not index >= self.size

def main() -> None:
    ll = LinkedList()

    print("Initial list (should be empty):")
    print(ll)
    print("Is empty?", ll.is_empty())
    print("Length:", len(ll))
    print()

    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("After appending 10, 20, 30:")
    print(ll)
    print("Length:", len(ll))
    print()

    ll.prepend(5)
    ll.prepend(2)
    print("After prepending 5, 2:")
    print(ll)
    print("Length:", len(ll))
    print()

    ll.remove(index=0)
    print("After removing index 0 (should remove 2):")
    print(ll)

    ll.remove(index=2)
    print("After removing index 2 (should remove 20):")
    print(ll)
    print()

    ll.remove(val=10)
    print("After removing value 10:")
    print(ll)
    print()

    print("Contains 20?", ll.contains(20))
    print("Contains 5?", ll.contains(5))
    print()

    node = ll.find(5)
    if node:
        print(f"Found node: {node}")
    else:
        print("Value not found")
    print()

    print("Final list:")
    print(ll)
    print("Length:", len(ll))


if __name__ == "__main__":
    main()