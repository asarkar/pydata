from __future__ import annotations

from collections.abc import Iterable, Iterator


class ListNode:
    """
    Linked List

    This class is an Iterator, so, you can write `list(mylist)` to turn it into a list.
    """

    def __init__(self, val: int) -> None:
        self.val = val
        self.next: ListNode | None = None
        self._node: ListNode | None = None

    def __repr__(self) -> str:
        return str(self.val)

    def __iter__(self) -> Iterator[int]:
        self._node = self
        return self

    def __next__(self) -> int:
        if self._node is not None:
            v = self._node.val
            self._node = self._node.next
            return v
        raise StopIteration

    @staticmethod
    def from_iterable(nums: Iterable[int]) -> ListNode | None:
        """Build a Linked List.

        :param nums: node values
        """

        head = prev = ListNode(0)
        for v in nums:
            prev.next = ListNode(v)
            prev = prev.next

        return head.next
