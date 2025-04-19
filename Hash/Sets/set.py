from Hash.HashTables.hash_table import HashTable


class Set:
    def __init__(self, capacity= 10):
        self.table = HashTable(capacity)

    def __str__(self):
        return str(self.table)

    def add(self, value):
        self.table[value] = True

    def remove(self, value):
        del self.table[value]

    def contains(self, value):
        return self.table[value] is not None

def main():
    s = Set()
    print("\nADD: 'apple'")
    s.add("apple")
    print(s)
    print("\nADD: 'banana'")
    s.add("banana")
    print(s)
    print("\nADD: 'orange'")
    s.add("orange")
    print(s)
    print("\nADD: 'banana'")
    s.add("banana")
    print(s)
    print("\nContains 'banana'? ->", s.contains("banana"))
    print("\nContains 'grape'? ->", s.contains("grape"))
    s.remove("banana")
    print("\nContains 'banana' after removal? →", s.contains("banana"))
    print(s)

if __name__ == "__main__":
    main()