from typing import Any


class LinearSearch:

    def __init__(self, arr : list[Any]):
        self.array = arr

    def __str__(self) -> str:
        return str(self.array)

    def __contains__(self, target : Any) -> bool:
        return self.search(target) is not None

    def search(self, target : Any) -> int | None:
        for i in range(len(self.array)):
            if self.array[i] == target:
                return i
        return None

def main():
    vals = [45, 77, 89, 90, 94, 99, 100]
    print("Linear Search: \n")
    int_linear_search = LinearSearch(vals)
    print(f"Find 99 in the array: {int_linear_search}\n")
    print(f"Index of 99: {int_linear_search.search(99)}\n")
    print(f"Index of 105: {int_linear_search.search(105)}\n")
    print(f"77 in the array? {77 in int_linear_search}\n")
    print(f"105 in the array? {105 in int_linear_search}\n")

if __name__ == "__main__":
    main()