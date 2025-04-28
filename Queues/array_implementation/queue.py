from typing import Any


class Queue:

    def __init__(self):
        self.queue : list[Any] = []

    def __str__(self) -> str:
        return f"\n{self.queue}"

    def __len__(self) -> int:
        return len(self.queue)

    def push(self, val : Any) -> None:
        if val is not None:
            self.queue.append(val)

    def pop(self) -> Any | None:
        try:
            return self.queue.pop(0)
        except IndexError:
            return None

    def peek(self) -> Any | None:
        try:
            return self.queue[0]
        except IndexError:
            return None

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