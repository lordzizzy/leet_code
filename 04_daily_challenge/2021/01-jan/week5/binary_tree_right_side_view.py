# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3630/

# Binary Tree Right Side View
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example:
# Input: [1,2,3,None,5,None,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

from typing import List
from termcolor import colored
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
    def rightSideView(self, root: TreeNode) -> List[int]:
        return self.rightSideView_recursive(root)

    def rightSideView_recursive(self, root: TreeNode) -> List[int]:
        def dfs(root: TreeNode, depth: int):
            if not root:
                return
            if depth >= len(res):
                res.append(root.val)
            dfs(root.right, depth+1)
            dfs(root.left, depth+1)

        res = []
        dfs(root, 0)
        return res

    def rightSideView_iterative(self, root: TreeNode) -> List[int]:
        res: List[int] = []
        cur_level: List[TreeNode] = [root] if root else None

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


def test_solution(nodes: List[int], expected: List[int]):
    def test_impl(func, nodes, expected):
        root = build_tree(nodes)
        r = func(root)
        if r == expected:
            print(
                colored(f"PASS {func.__name__} => tree: {nodes} right side view: {r}", "green"))
        else:
            print(colored(
                f"FAILED {func.__name__} => tree: {nodes} right side view: {r}, but expected: {expected}", "red"))
    sln = Solution()
    test_impl(sln.rightSideView_recursive, nodes, expected)
    test_impl(sln.rightSideView_iterative, nodes, expected)


if __name__ == "__main__":
    test_solution(nodes=[], expected=[])
    test_solution(nodes=[1, 2, 3, None, 5, None, 4], expected=[1, 3, 4])
    test_solution(nodes=[1, 2], expected=[1, 2])
