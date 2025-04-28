from __future__ import annotations
from typing import Any


class ListNode:

    def __init__(self, val) -> None:
        self.val : Any = val
        self.prev : ListNode | None = None
        self.next : ListNode | None = None

    def __str__(self) -> str:
        return f"Val: {self.val}"

    def get_val(self) -> Any:
        return self.val

    def get_prev(self) -> ListNode | None:
        return self.prev

    def get_next(self) -> ListNode | None:
        return self.next

    def set_val(self, val : Any) -> None:
        self.val = val

    def set_prev(self, prev : Any) -> None:
        self.prev = prev

    def set_next(self, next_node : ListNode) -> None:
        self.next = next_node
