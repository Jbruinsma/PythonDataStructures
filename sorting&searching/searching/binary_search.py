from typing import Any


class BinarySearch:

    def __init__(self, array : list[Any]):
        self.array : list[Any] = array

    def __str__(self):
        return str(self.array)

    def search(self, target : Any) -> int | None:
        return self.search_recursively(0, len(self.array) - 1, target)

    def __contains__(self, target : Any) -> bool:
        return self.search(target) is not None

    def search_recursively(self, start : int, end : int, target : Any) -> int | None:
        if start > end: return None
        mid = (start + end) // 2
        if self.array[mid] == target: return mid
        elif self.array[mid] > target: return self.search_recursively(start, mid - 1, target)
        else: return self.search_recursively(mid + 1, end, target)

def main():
    vals = [45, 77, 89, 90, 94, 99, 100]
    print("Binary Search: \n")
    int_binary_search = BinarySearch(vals)
    print(f"Find 99 in the array: {int_binary_search}\n")
    print(f"Index of 99: {int_binary_search.search(99)}\n")
    print(f"Index of 105: {int_binary_search.search(105)}\n")
    print(f"77 in the array? {77 in int_binary_search}\n")
    print(f"105 in the array? {105 in int_binary_search}\n")

if __name__ == "__main__":
    main()