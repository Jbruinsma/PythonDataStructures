from typing import Any

from Hash.HashTables.hash_table import HashTable


class HashMap:

    def __init__(self, capacity : int= 10) -> None:
        self.table = HashTable(capacity)

    def __setitem__(self, key : Any, value : Any) -> None:
        self.table[key] = value

    def __getitem__(self, key : Any) -> Any:
        return self.table[key]

    def remove(self, key : Any) -> None:
        del self.table[key]

    def contains(self, key : Any) -> bool:
        return self.table[key] is not None

    def __contains__(self, key : Any) -> bool:
        return self.table[key] is not None

    def __str__(self) -> str:
        return str(self.table)

def main():
    m = HashMap()
    print("Hash Map: \n")
    print(m, "\n")
    print("Adding: 'name': 'Alice'\n")
    m['name'] = "Alice"
    print(m, "\n")
    print("Adding: 'age': 25\n")
    m['age'] = 25
    print(m, "\n")
    print("Adding: 'city': 'New York'\n")
    m['city'] = 'New York'
    print(m, "\n")
    print("Updating: 'age': 26\n")
    m['age'] = 26
    print(m, "\n")
    print("Contains 'name'? ->", m.contains("name"), "\n")
    print("Contains 'email'? ->", "email" in m, "\n")
    m.remove("city")
    print("After removing 'city': \n")
    print(m, "\n")
    print("city ->", m['city'])

if __name__ == "__main__":
    main()
