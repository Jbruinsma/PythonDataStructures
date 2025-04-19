class HashTable:

    def __init__(self, capacity):
        self.CAPACITY = capacity
        self.table = [None] * capacity

    def __str__(self):
        items = []
        for bucket in self.table:
            if bucket is not None:
                for pair in bucket:
                    items.append(f'{pair[0]}: {pair[1]}')
        return '\n{' + ', '.join(items) + '}'

    def __setitem__(self, key, value):
        index = self._compute_hash(key)

        if self.table[index] is None:
            self.table[index] = [[key, value]]
        else:
            for pair in self.table[index]:
                if pair[0] == key:
                    pair[1] = value
                    return
            self.table[index].append([key, value])

    def __getitem__(self, key):
        return self.get(key, None)

    def __delitem__(self, key):
        index = self._compute_hash(key)
        if self.table[index] is None:
            return None
        else:
            for i, pair in enumerate(self.table[index]):
                if pair[0] == key:
                    del self.table[index][i]
                    return

    def get(self, key, replace= None):
        index = self._compute_hash(key)
        if self.table[index] is None:
            return replace
        else:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]

    def _compute_hash(self, key):
        return hash(key) % self.CAPACITY

def main():
    table = HashTable(5)
    table["apple"] = 10
    table["banana"] = 20
    table["orange"] = 30
    print(table)
    print("\napple:", table["apple"])
    print("\nbanana:", table["banana"])
    print("\norange:", table["orange"])
    print("\ngrape:", table["grape"])
    table["banana"] = 99
    print(table)
    print("\nbanana (updated):", table["banana"])
    del table["apple"]
    print("\napple (after deletion):", table["apple"])
    print("\nFinal table structure:")
    print(table)

if __name__ == '__main__':
    main()