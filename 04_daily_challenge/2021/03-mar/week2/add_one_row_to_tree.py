# # https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3666/

# Add One Row to Tree
# Given the root of a binary tree, then value v and depth d, you need to add a
# row of nodes with value v at the given depth d. The root node is at depth 1.

# The adding rule is: given a positive integer depth d, for each NOT None tree
# nodes N in depth d-1, create two tree nodes with value v as N's left subtree
# root and right subtree root. And N's original left subtree should be the left
# subtree of the new left subtree root, its original right subtree should be
# the right subtree of the new right subtree root. If depth d is 1 that means
# there is no depth d-1 at all, then create a tree node with value v as the new
# root of the whole original tree, and the original tree is the new root's left
# subtree.

# Example 1:
# Input:
# A binary tree as following:
#        4
#      /   \
#     2     6
#    / \   /
#   3   1 5
#
# v = 1
#
# d = 2
#
# Output:
#        4
#       / \
#      1   1
#     /     \
#    2       6
#   / \     /
#  3   1   5
#
# Example 2:
# Input:
# A binary tree as following:
#       4
#      /
#     2
#    / \
#   3   1
#
# v = 1
#
# d = 3
#
# Output:
#       4
#      /
#     2
#    / \
#   1   1
#  /     \
# 3       1
#
#
# Note:
# The given d is in range [1, maximum depth of the given tree + 1].
# The given binary tree has at least one tree node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Callable, Deque, List, Optional, Tuple
from shared.bst import TreeNode, build_list, build_tree
from termcolor import colored


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        return self.addOneRow_recursive_dfs(root, v, d)

    def addOneRow_recursive_dfs(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def traverse(node: TreeNode, v: int, lvl: int) -> TreeNode:
            if lvl + 1 == d:
                node.left = TreeNode(val=v, left=node.left)
                node.right = TreeNode(val=v, right=node.right)
            else:
                if node.left:
                    node.left = traverse(node.left, v, lvl + 1)
                if node.right:
                    node.right = traverse(node.right, v, lvl + 1)
            return node

        if d == 1:
            return TreeNode(val=v, left=root)

        return traverse(root, v, 1)

    def addOneRow_stack_dfs(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(val=v, left=root)

        stack: List[Tuple[TreeNode, int]] = [(root, 1)]

        while stack:
            node, depth = stack.pop()
            if node is None:
                continue
            if depth != d - 1:
                if node.left:
                    stack.append((node.left, depth + 1))
                if node.right:
                    stack.append((node.right, depth + 1))
            else:
                node.left = TreeNode(val=v, left=node.left)
                node.right = TreeNode(val=v, right=node.right)

        return root

    def addOneRow_queue_bfs(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(val=v, left=root)

        depth = 1
        q = Deque[TreeNode]([root])

        while depth < d - 1:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1

        while q:
            node = q.popleft()
            node.left = TreeNode(val=v, left=node.left)
            node.right = TreeNode(val=v, right=node.right)

        return root


NodeList = List[Optional[int]]
SolutionFunc = Callable[[TreeNode, int, int], TreeNode]


def test_solution(nodes: NodeList, v: int, d: int, expected: NodeList) -> None:
    def test_impl(
        func: SolutionFunc, nodes: NodeList, v: int, d: int, expected: NodeList
    ) -> None:
        root = build_tree(nodes)
        assert root is not None, f"root cannot be None."
        r = func(root, v, d)
        r_nodes = build_list(r)
        if r_nodes == build_list(build_tree(expected)):
            print(
                colored(
                    f"PASSED {func.__name__} => {nodes} with v={v} and d={d} is {r_nodes}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {nodes} with v={v} and d={d} is {r_nodes} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.addOneRow_recursive_dfs, nodes, v, d, expected)
    test_impl(sln.addOneRow_stack_dfs, nodes, v, d, expected)
    test_impl(sln.addOneRow_queue_bfs, nodes, v, d, expected)


if __name__ == "__main__":
    test_solution(
        nodes=[4, 2, 6, 3, 1, 5, None],
        v=1,
        d=2,
        expected=[4, 1, 1, 2, None, None, 6, 3, 1, 5, None],
    )

    test_solution(
        nodes=[4, 2, None, 3, 1],
        v=1,
        d=3,
        expected=[4, 2, None, 1, 1, 3, None, None, 1],
    )

    test_solution(
        nodes=[1, 2, 3, 4],
        v=5,
        d=4,
        expected=[1, 2, 3, 4, None, None, None, 5, 5],
    )
