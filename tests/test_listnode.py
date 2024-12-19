import random

import pytest

from src.pydata import ListNode


@pytest.mark.parametrize(
    "nums",
    [[], [1], [1, 2], [1, 2, 3, 4, 5]],
)
def test_list_is_the_dual_of_from_iterable(nums: list[int]) -> None:
    random.shuffle(nums)
    head = ListNode.from_iterable(nums)
    assert (not nums and head is None) or (head is not None and list(head) == nums)
