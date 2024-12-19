from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Generic, TypeVar

T = TypeVar("T")


class ListNode(Generic[T]):
    """
    Linked List

    This class is an Iterator, so, you can write `list(mylist)` to turn it into a list.
    """

    def __init__(self, val: T) -> None:
        self.val = val
        self.next: ListNode[T] | None = None
        self._node: ListNode[T] | None = None

    def __repr__(self) -> str:
        return str(self.val)

    def __iter__(self) -> Iterator[T]:
        self._node = self
        return self

    def __next__(self) -> T:
        if self._node is not None:
            v = self._node.val
            self._node = self._node.next
            return v
        raise StopIteration

    @staticmethod
    def from_iterable(nums: Iterable[T]) -> ListNode[T] | None:
        """Build a Linked List.

        :param nums: node values
        """
        head = prev = None
        for v in nums:
            if prev is None:
                head = prev = ListNode(v)
            else:
                prev.next = ListNode(v)
                prev = prev.next

        return head
