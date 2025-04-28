from typing import Any


class HashTable:

    def __init__(self, capacity : int) -> None:
        self.CAPACITY = capacity
        self.table = [None] * capacity

    def __str__(self) -> str:
        items: str = "{"
        first_element = True
        for bucket in self.table:
            if bucket is not None:
                for pair in bucket:
                    if not first_element:
                        items += ", "
                    else:
                        first_element = False
                    key = f"'{pair[0]}'" if isinstance(pair[0], str) else str(pair[0])
                    value = f"'{pair[1]}'" if isinstance(pair[1], str) else str(pair[1])
                    items += f"{key}: {value}"
        return items + "}"

    def __len__(self) -> int:
        count : int = 0
        for bucket in self.table:
            if bucket is not None:
                count += len(bucket)
        return count

    def __setitem__(self, key : Any, value : Any) -> None:
        index : int = self._compute_hash(key)

        if self.table[index] is None:
            self.table[index] = [[key, value]]
        else:
            for pair in self.table[index]:
                if pair[0] == key:
                    pair[1] = value
                    return
            self.table[index].append([key, value])

    def __getitem__(self, key : Any) -> Any:
        index: int = self._compute_hash(key)
        if self.table[index] is None:
            raise KeyError(f"Key {key} not found")
        else:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        raise KeyError(f"Key {key} not found")

    def __delitem__(self, key : Any) -> None:
        index : int = self._compute_hash(key)
        if self.table[index] is None:
            return None
        else:
            for i, pair in enumerate(self.table[index]):
                if pair[0] == key:
                    del self.table[index][i]
                    return None
                return None
            return None

    def __contains__(self, key : Any) -> bool:
        return self.get(key, None) is not None

    def get(self, key : Any, replace : Any = None) -> Any | None:
        index : int= self._compute_hash(key)
        if self.table[index] is None:
            return replace
        else:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
                return None
            return None

    def _compute_hash(self, key : Any) -> int:
        return hash(key) % self.CAPACITY

def main():
    table = HashTable(5)
    print("Hash Table: \n")
    print(table, "\n")
    print("Add: 'apple': \n")
    table["apple"] = 5
    print(table, "\n")
    print("Add: 'banana': \n")
    table["banana"] = 10
    print(table, "\n")
    print("Add: 'orange': \n")
    table["orange"] = 15
    print(table, "\n")
    print("Length of table:", len(table), "\n")
    print("Get 'apple':", table["apple"], "\n")
    print("Get 'banana':", table["banana"], "\n")
    print("Get 'orange':", table["orange"], "\n")
    print(f"'grape' in table? {'grape' in table}\n")
    print("Update 'banana' to 99\n")
    table["banana"] = 99
    print(table, "\n")
    print("Delete 'apple'\n")
    del table["apple"]
    print(table)

if __name__ == '__main__':
    main()