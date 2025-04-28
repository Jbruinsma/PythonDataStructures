from typing import Any

from Hash.HashTables.hash_table import HashTable


class Set:
    def __init__(self, capacity= 10) -> None:
        self.table = HashTable(capacity)

    def __str__(self) -> str:
        items: str = "{"
        first_element = True
        for bucket in self.table.table:
            if bucket is not None:
                for pair in bucket:
                    if not first_element:
                        items += ", "
                    else:
                        first_element = False

                    if isinstance(pair[0], str):
                        items += f"'{pair[0]}'"
                    else:
                        items += f"{pair[0]}"
        return items + "}"

    def add(self, value : Any) -> None:
        self.table[value] = True

    def remove(self, value : Any) -> None:
        del self.table[value]

    def contains(self, value : Any) -> bool:
        return self.table[value] is not None

    def __contains__(self, value : Any) -> bool:
        return self.contains(value) is not None

def main():
    s = Set()
    print("Hash Set: \n")
    print(s, "\n")
    print("ADD: 'apple'\n")
    s.add("apple")
    print(s, "\n")
    print("ADD: 'banana'\n")
    s.add("banana")
    print(s, "\n")
    print("ADD: 'orange'\n")
    s.add("orange")
    print(s, "\n")
    print("ADD: 'banana'\n")
    s.add("banana")
    print(s, "\n")
    print("Contains 'banana'? ->", "banana" in s )
    print("\nContains 'grape'? ->", s.contains("grape"))

if __name__ == "__main__":
    main()