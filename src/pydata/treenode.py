from __future__ import annotations

from collections import deque
from collections.abc import Iterator, Sequence
from typing import Generic, TypeVar

T = TypeVar("T")


class TreeNode(Generic[T]):
    """
    Binary Tree

    This class is an Iterator, so, you can write `list(tree)` to turn it into a list.
    The tree is traversed in level-order.
    """

    def __init__(self, val: T) -> None:
        self.val = val
        self.left: TreeNode[T] | None = None
        self.right: TreeNode[T] | None = None
        self._level: deque[TreeNode[T] | None] = deque()
        self._next_level: deque[TreeNode[T] | None] = deque()
        self._level_cnt: int = 1
        self._next_level_cnt: int = 0

    def __repr__(self) -> str:
        return str(self.val)

    def __str__(self) -> str:
        lines = TreeNode._build_tree_string(self, 0, False, "-")[0]
        return "\n" + "\n".join(line.rstrip() for line in lines)

    def __iter__(self) -> Iterator[T | None]:
        self._level.append(self)
        return self

    def __next__(self) -> T | None:
        if self._level_cnt == self._next_level_cnt == 0:
            raise StopIteration
        node = self._level.popleft()
        if node is not None:
            self._level_cnt -= 1
            for child in node.left, node.right:
                self._next_level_cnt += int(child is not None)
                self._next_level.append(child)
        if not self._level:
            self._level, self._next_level = self._next_level, self._level
            self._level_cnt, self._next_level_cnt = self._next_level_cnt, 0

        return node if node is None else node.val

    @staticmethod
    def from_seq(nums: Sequence[T | None]) -> TreeNode[T] | None:
        """Build a Binary Tree in level order.
        The idea is to take two numbers and associate with the
        first non-null parent that hasn't been looked at.

        :param nums: node values, could be None
        """

        queue: deque[TreeNode[T]] = deque()
        root = None
        if nums and nums[0] is not None:
            root = TreeNode(nums[0])
            queue.append(root)
        i = 1

        while i < len(nums):
            node = queue.popleft()
            if nums[i] is not None:
                node.left = TreeNode(nums[i])  # type: ignore[arg-type]
                queue.append(node.left)
            i += 1
            if i < len(nums) and nums[i] is not None:
                node.right = TreeNode(nums[i])  # type: ignore[arg-type]
                queue.append(node.right)
            i += 1

        queue.clear()

        print(nums)
        print(str(root))
        return root

    # Copied from binarytree.Node https://pypi.org/project/binarytree/
    @staticmethod
    def _build_tree_string(
        node: TreeNode[T] | None,
        curr_index: int,
        include_index: bool = False,
        delimiter: str = "-",
    ) -> tuple[list[str], int, int, int]:
        """Recursively walk down the binary tree and build a pretty-print string.

        In each recursive call, a "box" of characters visually representing the
        current (sub)tree is constructed line by line. Each line is padded with
        whitespaces to ensure all lines in the box have the same length. Then the
        box, its width, and start-end positions of its root node value repr string
        (required for drawing branches) are sent up to the parent call. The parent
        call then combines its left and right sub-boxes to build a larger box etc.

        :param node: Root node of the binary tree.
        :param curr_index: Level-order_ index of the current node (root node is 0).
        :param include_index: If set to True, include the level-order_ node indexes
            using the following format: ``{index}{delimiter}{value}`` (default: False).
        :param delimiter: Delimiter character between the node index and the node
            value (default: '-').
        :return: Box of characters visually representing the current subtree, width
            of the box, and start-end positions of the repr string of the new root
            node value.

        .. _Level-order:
            https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search
        """
        if node is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if include_index:
            node_repr = f"{curr_index}{delimiter}{node.val}"
        else:
            node_repr = str(node.val)

        new_root_width = gap_size = len(node_repr)

        # Get the left and right sub-boxes, their widths, and root repr positions
        l_box, l_box_width, l_root_start, l_root_end = TreeNode._build_tree_string(
            node.left, 2 * curr_index + 1, include_index, delimiter
        )
        r_box, r_box_width, r_root_start, r_root_end = TreeNode._build_tree_string(
            node.right, 2 * curr_index + 2, include_index, delimiter
        )

        # Draw the branch connecting the current root node to the left sub-box
        # Pad the line with whitespaces where necessary
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(" " * (l_root + 1))
            line1.append("_" * (l_box_width - l_root))
            line2.append(" " * l_root + "/")
            line2.append(" " * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        # Draw the representation of the current root node
        line1.append(node_repr)
        line2.append(" " * new_root_width)

        # Draw the branch connecting the current root node to the right sub-box
        # Pad the line with whitespaces where necessary
        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append("_" * r_root)
            line1.append(" " * (r_box_width - r_root + 1))
            line2.append(" " * r_root + "\\")
            line2.append(" " * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        # Combine the left and right sub-boxes with the branches drawn above
        gap = " " * gap_size
        new_box = ["".join(line1), "".join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else " " * l_box_width
            r_line = r_box[i] if i < len(r_box) else " " * r_box_width
            new_box.append(l_line + gap + r_line)

        # Return the new box, its width and its root repr positions
        return new_box, len(new_box[0]), new_root_start, new_root_end
