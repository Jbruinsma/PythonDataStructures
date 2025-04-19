class Queue:

    def __init__(self):
        self.queue = []

    def __str__(self):
        return f"\n{self.queue}"

    def __len__(self):
        return len(self.queue)

    def push(self, val):
        if val is not None:
            self.queue.append(val)

    def pop(self):
        try:
            return self.queue.pop(0)
        except IndexError:
            return None

    def peek(self):
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