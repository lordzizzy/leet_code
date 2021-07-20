# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3819/

# Lowest Common Ancestor of a Binary Search Tree
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.


# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”

# Input: root = [6,2,8,0,4,7,9,None,None,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Example 2:
# Input: root = [6,2,8,0,4,7,9,None,None,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
# of itself according to the LCA definition.

# Example 3:
# Input: root = [2,1], p = 2, q = 1
# Output: 2

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the BST.

from typing import Callable, List, Optional

from shared import bst
from termcolor import colored

TreeNode = bst.TreeNode
NodeList = List[Optional[int]]


def find_node(root: TreeNode, val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    if root.left and (node := find_node(root.left, val)):
        return node
    if root.right and (node := find_node(root.right, val)):
        return node
    return None


class Solution:
    def lowestCommonAncestor_recursive(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor_recursive(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor_recursive(root.left, p, q)
        else:
            return root

    def lowestCommonAncestor_iterative(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        p_val, q_val = p.val, q.val
        stack = [root]

        while stack:
            node = stack.pop()
            if p_val > node.val and q_val > node.val:
                stack.append(node.right)
            elif p_val < node.val and q_val < node.val:
                stack.append(node.left)
            else:
                return node

        return root


SolutionFunc = Callable[[TreeNode, TreeNode, TreeNode], TreeNode]


def test_solution(nodes: NodeList, p_val: int, q_val: int, expected: int) -> None:
    def test_impl(
        func: SolutionFunc, nodes: NodeList, p_val: int, q_val: int, expected: int
    ) -> None:
        root = bst.build_tree(nodes)
        assert root, "root cannot be None"
        p = find_node(root, p_val)
        assert p, "p cannot be None"
        q = find_node(root, q_val)
        assert q, "q cannot be None"

        res = func(root, p, q)
        assert res, "res cannot be None"
        if res.val == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Lowest common ancestor of {p_val} and {q_val} in tree {nodes} is {res.val}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Lowest common ancestor of {p_val} and {q_val} in tree {nodes} is {res.val} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.lowestCommonAncestor_recursive, nodes, p_val, q_val, expected)
    test_impl(sln.lowestCommonAncestor_iterative, nodes, p_val, q_val, expected)


if __name__ == "__main__":
    test_solution(
        nodes=[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p_val=2, q_val=4, expected=2
    )
    test_solution(nodes=[2, 1], p_val=2, q_val=1, expected=2)
