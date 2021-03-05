# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3661/

# Average of Levels in Binary Tree
# Given a non-empty binary tree, return the average value of the nodes on each
# level in the form of an array.

# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level
# 2 is 11. Hence return [3, 14.5, 11].
# Note:
# The range of node's value is in the range of 32-bit signed integer.

from collections import deque
from typing import Callable, DefaultDict, Deque, List, Optional
from shared.bst import TreeNode, build_tree
from termcolor import colored


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        return self.averageOfLevels_hashtable(root)

    def averageOfLevels_hashtable(self, root: Optional[TreeNode]) -> List[float]:
        d = DefaultDict[int, List[float]](lambda: [])

        def traverse(root: Optional[TreeNode], level: int):
            if not root:
                return
            d[level].append(root.val)
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)

        traverse(root, 0)
        # note: this iteration depends on 2 things:
        # 1. the preorder traversal guarantees the level keys get inserted inorder
        # 2. the insertion order of python dictionaries from python ver 3.7+
        return [sum(nums) / len(nums) for _, nums in d.items()]

    def averageOfLevels_iterative(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        q: Deque[TreeNode] = deque([root])
        ans: List[float] = []
        while q:
            n = len(q)
            total = 0
            for _ in range(n):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(total / n)
        return ans


SolutionFunc = Callable[[Optional[TreeNode]], List[float]]


def test_solution(nodes: List[Optional[int]], expected: List[float]) -> None:
    def test_impl(
        func: SolutionFunc, nodes: List[Optional[int]], expected: List[float]
    ) -> None:
        root = build_tree(nodes)
        r = func(root)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {nodes} average level values are {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {nodes} average level values are {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.averageOfLevels_hashtable, nodes, expected)
    test_impl(sln.averageOfLevels_iterative, nodes, expected)


if __name__ == "__main__":
    test_solution(nodes=[3, 9, 20, None, None, 15, 7], expected=[3, 14.5, 11])
