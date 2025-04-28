from typing import Any

from Hash.HashTables.hash_table import HashTable


class HashMap(HashTable):

    def __init__(self, capacity: int = 10) -> None:
        super().__init__(capacity)

    def __str__(self) -> str:
        return super().__str__()

    def __setitem__(self, key: Any, value: Any) -> None:
        super().__setitem__(key, value)

    def __getitem__(self, key: Any) -> Any:
        return super().__getitem__(key)

    def __delitem__(self, key: Any) -> None:
        super().__delitem__(key)

    def __contains__(self, key: Any) -> bool:
        return super().get(key) is not None

    def get(self, key: Any, replace: Any = None) -> Any:
        return super().get(key, replace)

    def remove(self, key: Any) -> None:
        super().__delitem__(key)

    def contains(self, key: Any) -> bool:
        return super().get(key) is not None

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
    print("city ->", m.get("city"), "\n")

if __name__ == "__main__":
    main()
