import pytest

from src.pydata import TreeNode


@pytest.mark.parametrize(
    "nums",
    [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, None, 2],
        [1, 2, None, 3],
        [4, 2, 5, 1, 3],
        [3, 1, 4, None, 2],
        [1, 3, 2, 5, 3, None, 9],
        [10, 5, 15, 3, 7, None, 18],
        [7, 3, 15, None, None, 9, 20],
        [1, 2, 3, None, None, 4, 5, 6, 7],
        [10, 5, 15, 3, 7, 13, 18, 1, None, 6],
        [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
    ],
)
def test_list_is_the_dual_of_from_seq(nums: list[int | None]) -> None:
    root = TreeNode.from_seq(nums)
    assert (not nums and root is None) or (root is not None and list(root) == nums)
