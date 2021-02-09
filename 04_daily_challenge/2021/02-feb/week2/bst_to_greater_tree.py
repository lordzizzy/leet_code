# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3634/

# Convert BST to Greater Tree
# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/


# Example 1:
# Input: root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
# Output: [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]

# Example 2:
# Input: root = [0,None,1]
# Output: [1,None,1]

# Example 3:
# Input: root = [1,0,2]
# Output: [3,3,2]

# Example 4:
# Input: root = [3,2,4,1]
# Output: [7,9,4,10]


# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
# -10^4 <= Node.val <= 10^4
# All the values in the tree are unique.
# root is guaranteed to be a valid binary search tree.

from __future__ import annotations
from typing import Any, Callable, List
from termcolor import colored
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.val: int = val
        self.left: TreeNode = left
        self.right: TreeNode = right

    def __str__(self) -> str:
        return f"<{self.val} {self.left}, {self.right}>"


def build_tree(nodes) -> TreeNode:
    if not nodes:
        return None
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
    if not root:
        return []
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
    def convertBST(self, root: TreeNode) -> TreeNode:
        return self.convertBST_recursive(root)

    def convertBST_recursive(self, root: TreeNode) -> TreeNode:
        def visit(node: TreeNode):
            if not node:
                return
            nonlocal sum
            visit(node.right)
            sum += node.val
            node.val = sum
            visit(node.left)
        sum = 0
        visit(root)
        return root

    def convertBST_iterative(self, root: TreeNode) -> TreeNode:
        sum = 0
        stack = []
        node = root
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.right
            node = stack.pop()
            sum += node.val
            node.val = sum
            node = node.left
        return root


def test_solution(nodes: List[Any], expected: List[Any]):
    def test_impl(func: Callable[[TreeNode], TreeNode], nodes: List[Any], expected: List[Any]):
        root = build_tree(nodes)
        r = func(root)
        r_nodes = build_list(r)
        e_nodes = build_list(build_tree(expected))
        if r_nodes == e_nodes:
            print(colored(
                f"PASSED {func.__name__} => bst:{nodes} to greater tree is: {r_nodes}", "green"))
        else:
            print(colored(
                f"FAILED {func.__name__} => bst:{nodes} to greater tree is: {r_nodes}, expected: {e_nodes}", "red"))
    sln = Solution()
    test_impl(sln.convertBST, nodes, expected)
    test_impl(sln.convertBST_iterative, nodes, expected)


if __name__ == "__main__":
    test_solution(nodes=[4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8], expected=[
                  30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8])
    test_solution(nodes=[0, None, 1], expected=[1, None, 1])
    test_solution(nodes=[1, 0, 2], expected=[3, 3, 2])
    test_solution(nodes=[3, 2, 4, 1], expected=[7, 9, 4, 10])
