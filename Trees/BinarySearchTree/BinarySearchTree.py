from Trees.BinarySearchTree.tree_node import TreeNode
from typing import Any

class BinarySearchTree:

    def __init__(self, val: Any= None, array : list[Any]= None) -> None:
        self.root : TreeNode | None = None
        if val is not None:
            self.root = TreeNode(val)
            return
        elif array is not None and len(array) > 0:
            self.root = TreeNode(array[0])
            for i in range(1, len(array)):
                self.root.insert(array[i])

    def __str__(self) -> str:
        def to_tuple(node):
            if node is None: return None
            return node.val, to_tuple(node.left), to_tuple(node.right)
        return str(to_tuple(self.root))

    def to_array(self) -> list[Any]:
        return self.root.in_order()

    def insert(self, val: Any= None, array: list[Any]=None) -> None:
        if val is not None:
            if self.is_empty():
                self.root = TreeNode(val)
            else:
                self.root.insert(val)
        elif array is not None and len(array) > 0:
            if self.is_empty(): self.root = TreeNode(array[0])
            for i in range(1, len(array)):
                self.root.insert(array[i])
        else:
            raise ValueError("Must provide a value or an array to insert.")

    def delete(self, val: Any) -> None:
        self.root = self.root.delete(val)

    def contains(self, val : Any) -> bool:
        return self.root.contains(val)

    def find(self, val : Any) -> TreeNode | None:
        return self.root.find(val)

    def pre_order_traversal(self) -> list[Any]:
        return self.root.pre_order()

    def in_order_traversal(self) -> list[Any]:
        return self.root.in_order()

    def post_order_traversal(self) -> list[Any]:
        return self.root.post_order()

    def level_order_traversal(self) -> list[Any]:
        return self.root.level_order()

    def find_min_val(self) -> Any:
        return self.root.min_val()

    def find_max_val(self) -> Any:
        return self.root.max_val()

    def height(self) -> int:
        return self.root.height()

    def size(self) -> int:
        return self.root.size()

    def is_empty(self) -> bool:
        return self.root is None

def main():
    RED = "\033[91m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

    arr1 = [6, 5, 3, 4, 2, 1, 7, 9, 8, 10]
    arr2 = [8, 3, 5, 10, 1]
    bst = BinarySearchTree()

    print(f"{RED}Binary Search Tree:{RESET}")
    bst.insert(array=arr1)
    print(f"{WHITE}{bst}\n")

    print(f"{RED}To sorted array:{RESET}")
    print(f"{WHITE}{bst.to_array()}\n")

    print(f"{RED}Pre Order Traversal:{RESET}")
    print(f"{WHITE}{bst.pre_order_traversal()}\n")

    print(f"{RED}In Order Traversal:{RESET}")
    print(f"{WHITE}{bst.in_order_traversal()}\n")

    print(f"{RED}Post Order Traversal:{RESET}")
    print(f"{WHITE}{bst.post_order_traversal()}\n")

    print(f"{RED}Level Order Traversal:{RESET}")
    print(f"{WHITE}{bst.level_order_traversal()}\n")

    print(f"{RED}Tree height:{RESET}")
    print(f"{WHITE}{bst.height()}\n")

    print(f"{RED}Tree Size:{RESET}")
    print(f"{WHITE}{bst.size()}\n")

    print(f"{RED}Contains 8?{RESET}")
    print(f"{WHITE}{bst.contains(8)}\n")

    print(f"{RED}Contains 50?{RESET}")
    print(f"{WHITE}{bst.contains(50)}\n")

    print(f"{RED}Find 10?{RESET}")
    print(f"{WHITE}{bst.find(10)}\n")

    print(f"{RED}Find 100?{RESET}")
    print(f"{WHITE}{bst.find(15)}\n")

    print(f"{RED}Delete 10:{RESET}")
    print(f"{WHITE}{bst.level_order_traversal()}\n")

    bst.delete(10)

    print(f"{WHITE}{bst.level_order_traversal()}\n")


if __name__ == "__main__":
    main()