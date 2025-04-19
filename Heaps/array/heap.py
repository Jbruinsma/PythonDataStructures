class Heap:

    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def __len__(self):
        return len(self.heap)

    def insert(self, val):
        if val is not None:
            index = len(self)
            self.heap.append(val)
            self.bubble_up(index)

    def remove_min(self):
        self._swap(0, len(self) - 1)
        min_val = self.heap.pop()
        self.bubble_down(0)
        return min_val

    def bubble_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[parent_index] > self.heap[index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2

    def bubble_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest_child_index = index
            if left_child_index < len(self) and self.heap[left_child_index] < self.heap[smallest_child_index]:
                smallest_child_index = left_child_index
            if right_child_index < len(self) and self.heap[right_child_index] < self.heap[smallest_child_index]:
                smallest_child_index = right_child_index
            if smallest_child_index == index: break
            self._swap(index, smallest_child_index)
            index = smallest_child_index

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

def main():
    h = Heap()
    for val in [50, 30, 10, 5]:
        h.insert(val)
        print(h)
    print(f'MIN VAL: {h.remove_min()}')
    print(h)

if __name__ == '__main__':
    main()
