# Python Data Structures
Python Package containing simple data structures used in data structure and algorithm questions 
found on online platform such as LeetCode. This package can be used while working on such
questions locally.

Meant to be used in personal projects only, and makes absolutely no guarantees.

[![](https://github.com/asarkar/pydata/workflows/CI/badge.svg)](https://github.com/asarkar/pydata/actions)

## Development

```
pydata% $(brew --prefix python)/bin/python3 -m venv ./venv

pydata% ./venv/bin/python -m pip install --upgrade pip '.[test]' '.[lint]'
```

## Usage

* [ListNode](src/pydata/listnode.py)

```
nums = [1, 2, 3]
head = ListNode.from_iterable(nums)
assert head is not None and list(head) == nums
```
* [TreeNode](src/pydata/treenode.py)

```
nums = [1, 2, 3]
root = TreeNode.from_seq(nums)
assert root is not None and list(root) == nums

print(str(root))
  1
 / \
2   3
```

## Running tests
```
./.github/run.sh
```

## License

Released under [Apache License v2.0](LICENSE).
