# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3626/

# Trim a Binary Search Tree

# Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.
# Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.

# Input: root = [3,0,4,None,2,None,None,1], low = 1, high = 3
# Output: [3,2,None,1]
# Example 3:

# Input: root = [1], low = 1, high = 2
# Output: [1]

# Example 4:
# Input: root = [1,None,2], low = 1, high = 3
# Output: [1,None,2]

# Example 5:
# Input: root = [1,None,2], low = 2, high = 4
# Output: [2]

# Constraints:
# The number of nodes in the tree in the range [1, 10^4].
# 0 <= Node.val <= 10^4
# The value of each node in the tree is unique.
# root is guaranteed to be a valid binary search tree.
# 0 <= low <= high <= 10^4

from __future__ import annotations
from termcolor import colored
from typing import List
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right

    def __str__(self) -> str:
        return f"<{self.val} {self.left}, {self.right}>"


def build_tree(nodes) -> TreeNode:
    it = iter(nodes)
    tree = TreeNode(next(it))
    fringe = deque([tree])
    while len(fringe) > 0:
        head = fringe.popleft()
        try:
            l_val = next(it)
            if l_val is not None:
                head.left = TreeNode(l_val)
                fringe.append(head.left)
            r_val = next(it)
            if r_val:
                head.right = TreeNode(r_val)
                fringe.append(head.right)
        except StopIteration:
            break
    return tree


def build_list(root: TreeNode):
    lst = []
    fringe = deque([root])
    lst.append(root.val)
    while len(fringe) > 0:
        head = fringe.popleft()
        if head.left:
            lst.append(head.left.val)
            fringe.append(head.left)
        else:
            lst.append(None)
        if head.right:
            lst.append(head.right.val)
            fringe.append(head.right)
        else:
            lst.append(None)
    return lst


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        return self.trimBST_iterative(root, low, high)
        # return self.trimBST_recursive(root, low, high)

    def trimBST_recursive(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trim(node: TreeNode) -> TreeNode:
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
        return trim(root)

    def trimBST_iterative(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # find real root to return
        while root and not (low <= root.val <= high):
            if root.val > high:
                root = root.left
            elif root.val < low:
                root = root.right

        stack = [root]
        while stack:
            node = stack[-1]
            if not node:
                stack.pop()
                continue
            update = 0
            if node.left and node.left.val < low:
                node.left = node.left.right
                update += 1
            elif node.right and node.right.val > high:
                node.right = node.right.left
                update += 1
            if not update:
                stack.pop()
                stack.append(node.left)
                stack.append(node.right)
        return root


def test_solution(nodes, low, high, expected):
    def test_impl(func, nodes, low, high, expected) -> TreeNode:
        root = build_tree(nodes)
        root = func(root, low, high)
        r = build_list(root)
        if r == build_list(build_tree(expected)):
            print(
                colored(f"PASSED {func.__name__}=> binary tree of {nodes} with range min={low}, max={high} trimmed is {r}", "green"))
        else:
            print(colored(
                f"FAILED {func._name__}=> binary tree of {nodes} with range min={low}, max={high} trimmed is {r}, expected; {expected}", "red"))
    sln = Solution()
    test_impl(sln.trimBST_iterative, nodes, low, high, expected)
    test_impl(sln.trimBST_recursive, nodes, low, high, expected)


if __name__ == "__main__":
    test_solution(nodes=[3, 0, 4, None, 2, None, None, 1],
                  low=1, high=3, expected=[3, 2, None, 1])

    test_solution(nodes=[3, 2, 4, 1],
                  low=1, high=1, expected=[1])

    test_solution(nodes=[1],
                  low=1, high=2, expected=[1])

    test_solution(nodes=[1, None, 2],
                  low=1, high=3, expected=[1, None, 2])

    test_solution(nodes=[1, None, 2],
                  low=2, high=4, expected=[2])
