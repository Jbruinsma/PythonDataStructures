class BinarySearch:

    def __init__(self, arr):
        self.arr = arr

    def get_array(self): return self.arr

    def get_array_length(self): return len(self.arr)

    def search(self, start, end, key):
        if start > end:
            return False

        mid = start + (end - start) // 2

        if self.arr[mid] == key:
            return True
        elif key < self.arr[mid]: return  self.search(0, mid - 1, key)
        else: return self.search(mid + 1, end, key)


bs = BinarySearch([45, 77, 89, 90, 94, 99, 100, 105])
print(bs.search(0, bs.get_array_length(), 44))