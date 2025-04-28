from typing import Any


class Heap:

    def __init__(self) -> None:
        self.heap : list[Any] = []

    def __str__(self) -> str:
        return str(self.heap)

    def __len__(self) -> int:
        return len(self.heap)

    def insert(self, val: Any) -> None:
        if val is not None:
            index : int = len(self)
            self.heap.append(val)
            self.bubble_up(index)

    def remove_min(self) -> Any | None:
        self._swap(0, len(self) - 1)
        min_val : Any = self.heap.pop()
        self.bubble_down(0)
        return min_val

    def bubble_up(self, index : int) -> None:
        parent_index : int = (index - 1) // 2
        while index > 0 and self.heap[parent_index] > self.heap[index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2

    def bubble_down(self, index : int) -> None:
        while True:
            left_child_index : int = 2 * index + 1
            right_child_index : int = 2 * index + 2
            smallest_child_index : int = index
            if left_child_index < len(self) and self.heap[left_child_index] < self.heap[smallest_child_index]:
                smallest_child_index = left_child_index
            if right_child_index < len(self) and self.heap[right_child_index] < self.heap[smallest_child_index]:
                smallest_child_index = right_child_index
            if smallest_child_index == index: break
            self._swap(index, smallest_child_index)
            index = smallest_child_index

    def _swap(self, index1 : int, index2 : int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

def main() -> None:
    h = Heap()
    print("Min Heap: \n")
    print(h, "\n")
    print("Inserting: 50, 30, 10, 5\n")
    for val in [50, 30, 10, 5]:
        h.insert(val)
        print(h, "\n")
    print(f'Remove root: {h.remove_min()}\n')
    print(h)

if __name__ == '__main__':
    main()
