from LinkedLists.linked_list import LinkedList
from typing import Any


class Queue:
    def __init__(self) -> None:
        self.queue = LinkedList()

    def __str__(self) -> str:
        q_str : list[Any] = []
        curr = self.queue.head
        while curr:
            q_str.append(curr.val)
            curr = curr.next
        return str(q_str)

    def __len__(self) -> int:
        return self.queue.size

    def push(self, val : Any) -> None:
        if val is not None:
            self.queue.append(val)

    def pop(self) -> Any | None:
        if self.queue.head is None:
            return None
        else:
            val = self.queue.head.val
            self.queue.remove(val)
            return val

    def peek(self) -> Any | None:
        if self.queue.head is None:
            return None
        else:
            return self.queue.head.val


def main():
    q = Queue()
    print(q)
    print("PUSH: 1")
    q.push(1)
    print(q)
    print("PUSH: 2")
    q.push(2)
    print(q)
    print("PUSH: 3")
    q.push(3)
    print(q)
    print(f"POP: Result: {q.pop()}")
    print(q)
    print(f"POP: Result: {q.pop()}")
    print(q)
    print(f'PEEK: Result: {q.peek()}')

if __name__ == '__main__':
    main()