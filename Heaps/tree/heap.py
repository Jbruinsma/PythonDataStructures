from Heaps.tree.heap_node import HeapNode


class Heap:

    def __init__(self):
        self.root = None

    def insert(self, val):
        if val is not None:
            if self.root is None:
                self.root = HeapNode(val)
            else:
                inserted_node = self.root.insert(val)
                inserted_node.bubble_up()

    def get_root_val(self):
        if self.root is None:
            return None
        else:
            return self.root.val

    def is_empty(self):
        return self.root is None

def main():
    heap = Heap()
    print(heap.get_root_val())
    heap.insert(50)
    print(heap.get_root_val())
    heap.insert(30)
    print(heap.get_root_val())
    heap.insert(10)
    print(heap.get_root_val())
    heap.insert(5)
    print(heap.get_root_val())
    heap.insert(20)
    print(heap.get_root_val())

if __name__ == '__main__':
    main()
