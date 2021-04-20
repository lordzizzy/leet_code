# N-ary Tree Preorder Traversal
# Given the root of an n-ary tree, return the preorder traversal of its nodes'
# values.

# Nary-Tree input serialization is represented in their level order traversal.
# Each group of children is separated by the None value (See examples)

# Example 1:
# Input: root = [1,None,3,2,4,None,5,6]
# Output: [1,3,5,6,2,4]

# Example 2:
# Input: root =
# [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,
#  13,None,None,14]

# Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]


# Constraints:
# The number of nodes in the tree is in the range [0, 10⁴].
# 0 <= Node.val <= 10⁴
# The height of the n-ary tree is less than or equal to 1000.

# Follow up: Recursive solution is trivial, could you do it iteratively?

from __future__ import annotations
from typing import Callable, Deque, List, Optional
from termcolor import colored

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, children: Optional[List[Node]] = None):
        self.val = val
        self.children = children


def build_nary_tree(node_list: List[Optional[int]]) -> Optional[Node]:
    q = Deque[Optional[int]](node_list)
    res = Deque[Node]()
    root = Node(val=q.popleft())
    assert root.val, "Root cannot be None"
    v = q.popleft()
    assert v is None, "Value after root should be None"
    curr = root
    while q:
        value = q.popleft()
        if value is None:
            curr = res.popleft()
        else:
            node = Node(val=value)
            if not curr.children:
                curr.children = []
            curr.children.append(node)
            res.append(node)
    return root


class Solution:
    def preorder(self, root: Node) -> List[int]:
        return self.preorder_recursive(root)

    def preorder_recursive(self, root: Node) -> List[int]:
        res: List[int] = []

        def traverse(node: Node) -> None:
            if node:
                res.append(node.val)
                if node.children:
                    for i in range(len(node.children)):
                        traverse(node.children[i])

        traverse(root)
        return res

    def preorder_iterative(self, root: Node) -> List[int]:
        res: List[int] = []
        # todo: use a stack
        return res


SolutionFunc = Callable[[Node], List[int]]


def test_solution(nodes: List[Optional[int]], expected: List[int]) -> None:
    def test_impl(
        func: SolutionFunc, nodes: List[Optional[int]], expected: List[int]
    ) -> None:
        root = build_nary_tree(nodes)
        assert root, f"Root cannot be None"
        r = func(root)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => N-ary Tree Preorder Traversal for {nodes} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => N-ary Tree Preorder Traversal for {nodes} is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.preorder_recursive, nodes, expected)


if __name__ == "__main__":
    test_solution(nodes=[1, None, 3, 2, 4, None, 5, 6], expected=[1, 3, 5, 6, 2, 4])

    test_solution(
        nodes=[
            1,
            None,
            2,
            3,
            4,
            5,
            None,
            None,
            6,
            7,
            None,
            8,
            None,
            9,
            10,
            None,
            None,
            11,
            None,
            12,
            None,
            13,
            None,
            None,
            14,
        ],
        expected=[1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10],
    )
