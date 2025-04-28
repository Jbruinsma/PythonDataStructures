from typing import Any


class Stack:

    def __init__(self) -> None:
        self.stack : list[Any] = []

    def __str__(self) -> str:
        return f"\n{self.stack}"

    def __len__(self) -> int:
        return len(self.stack)

    def push(self, val : Any) -> None:
        if val is not None:
            self.stack.append(val)

    def pop(self) -> Any | None:
        return self.stack.pop()

    def peek(self) -> Any | None:
        try:
            return self.stack[-1]
        except IndexError:
            return None

def main():
    stack = Stack()
    print(stack)
    print(f'PUSH 10')
    stack.push(10)
    print(stack)
    print(f'PUSH 20')
    stack.push(20)
    print(stack)
    print(f'PUSH 30')
    stack.push(30)
    print(stack)
    print(f'\nPOP: Result: {stack.pop()}')
    print(stack)
    print(f'\nPEEK: Result: {stack.peek()}')
    print(stack)

if __name__ == '__main__':
    main()