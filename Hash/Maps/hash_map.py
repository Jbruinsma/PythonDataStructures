from Hash.HashTables.hash_table import HashTable


class HashMap:

    def __init__(self, capacity= 10):
        self.table = HashTable(capacity)

    def __setitem__(self, key, value):
        self.table[key] = value

    def __getitem__(self, key):
        return self.table[key]

    def remove(self, key):
        del self.table[key]

    def contains(self, key):
        return self.table[key] is not None

    def __str__(self):
        return str(self.table)

def main():
    m = HashMap()
    print("\nAdding: 'name': 'Alice'")
    m['name'] = "Alice"
    print(m)
    print("\nAdding: 'age': 25")
    m['age'] = 25
    print(m)
    print("\nAdding: 'city': 'New York'")
    m['city'] = 'New York'
    print(m)
    print("\nUpdating: 'age': 26")
    m['age'] = 26
    print(m)
    print("\nContains 'name'? ->", m.contains("name"))
    print("\nContains 'email'? ->", m.contains("email"))
    m.remove("city")
    print("\nAfter removing 'city':")
    print(m)
    print("\ncity ->", m['city'])

if __name__ == "__main__":
    main()
