# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3749/

# Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).

# Example 1:
# Example 1:
# Input: root = [3,9,20,None,None,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

from typing import Callable, List, Optional
from termcolor import colored

from shared import bst

TreeNode = bst.TreeNode
NodeList = List[Optional[int]]


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.levelOrder_recursive(root)

    def levelOrder_recursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res: List[List[int]] = []

        def traverse(node: TreeNode, lvl: int):
            nonlocal res
            if len(res) <= lvl:
                res.append([])
            res[lvl].append(node.val)
            if node.left:
                traverse(node.left, lvl + 1)
            if node.right:
                traverse(node.right, lvl + 1)

        traverse(root, 0)

        return res

    def levelOrder_iterative(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q: List[TreeNode] = [root]
        res: List[List[int]] = []
        while len(q):
            l: List[int] = []
            for _ in range(len(q)):
                node = q.pop(0)  # note: this is O(N) not O(1), consider using deque?
                l.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(l)
        return res


SolutionFunc = Callable[[Optional[TreeNode]], List[List[int]]]


def test_solution(nodes: NodeList, expected: List[List[int]]) -> None:
    def test_impl(
        func: SolutionFunc, nodes: NodeList, expected: List[List[int]]
    ) -> None:
        root = bst.build_tree(nodes)
        r = func(root)
        if sorted(r) == sorted(expected):
            print(
                colored(
                    f"PASSED {func.__name__} => Level ordered traversal of {nodes} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Level ordered traversal of {nodes} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.levelOrder_recursive, nodes, expected)
    test_impl(sln.levelOrder_iterative, nodes, expected)


if __name__ == "__main__":
    test_solution(nodes=[3, 9, 20, None, None, 15, 7], expected=[[3], [9, 20], [15, 7]])
    test_solution(nodes=[1], expected=[[1]])
    test_solution(nodes=[], expected=[])
