# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3630/

# Binary Tree Right Side View
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.

# Example:
# Input: [1,2,3,None,5,None,4]
# Output: [1, 3, 4]
# Explanation:
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

from typing import Callable, List, Optional
from termcolor import colored
from shared import bst

TreeNode = bst.TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.rightSideView_recursive(root)

    def rightSideView_recursive(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: Optional[TreeNode], depth: int):
            if not root:
                return
            if depth >= len(res):
                res.append(root.val)
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)

        res = []
        dfs(root, 0)
        return res

    def rightSideView_iterative(self, root: Optional[TreeNode]) -> List[int]:
        res: List[int] = []
        cur_level: List[TreeNode] = [root] if root else []

        while cur_level:
            res.append(cur_level[-1].val)
            next_level: List[TreeNode] = []
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level = next_level
        return res


SolutionFunc = Callable[[Optional[TreeNode]], List[int]]


def test_solution(nodes: List[Optional[int]], expected: List[int]):
    def test_impl(func: SolutionFunc, nodes: List[Optional[int]], expected: List[int]):
        root = bst.build_tree(nodes)
        r = func(root)
        if r == expected:
            print(
                colored(
                    f"PASS {func.__name__} => tree: {nodes} right side view: {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => tree: {nodes} right side view: {r}, but expected: {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.rightSideView_recursive, nodes, expected)
    test_impl(sln.rightSideView_iterative, nodes, expected)


if __name__ == "__main__":
    test_solution(nodes=[], expected=[])
    test_solution(nodes=[1, 2, 3, None, 5, None, 4], expected=[1, 3, 4])
    test_solution(nodes=[1, 2], expected=[1, 2])
