# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/607/week-5-june-29th-june-30th/3797/

# Lowest Common Ancestor of a Binary Tree
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


# Example 1:
# Input: root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:
# Input: root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.

# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1


# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -10⁹ <= Node.val <= 10⁹
# All Node.val are unique.
# p != q
# p and q will exist in the tree.

from typing import Callable, List, Optional

from shared import bst
from termcolor import colored

TreeNode = bst.TreeNode


def find_node(root: TreeNode, val: int) -> Optional[TreeNode]:
    if root.val == val:
        return root

    if root.left and (node := find_node(root.left, val)):
        return node

    if root.right and (node := find_node(root.right, val)):
        return node

    return None


class Solution:
    # reference
    # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65225/4-lines-C%2B%2BJavaPythonRuby
    #
    # NOTE: this solution will traverse all nodes because of the flow, so we
    # can optimize it to short circuit if p or q on the left subtree
    # Time complexity: O(N)
    # Space complexity: O(N)
    def lowestCommonAncestor_recursive(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        def find(
            root: Optional[TreeNode], p: TreeNode, q: TreeNode
        ) -> Optional[TreeNode]:
            if root in (None, p, q):
                return root
            left, right = (find(child, p, q) for child in (root.left, root.right))
            return root if left and right else left or right

        return find(root, p, q)

    def lowestCommonAncestor_recursive_fast(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        if not root:
            return root

        if root == p or root == q:
            return root

        l = self.lowestCommonAncestor_recursive_fast(root.left, p, q)
        r = self.lowestCommonAncestor_recursive_fast(root.right, p, q)

        if l and r:
            return root

        return l or r

    # reference
    # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65245/Iterative-Solutions-in-PythonC%2B%2B
    #
    # Time complexity: O(N)
    # Space complexity: O(N)
    def lowestCommonAncestor_iterative(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        pass


SolutionFunc = Callable[[TreeNode, TreeNode, TreeNode], Optional[TreeNode]]


def test_solution(
    tree_nodes: List[Optional[int]], p: int, q: int, expected: int
) -> None:
    def test_impl(
        func: SolutionFunc,
        tree_nodes: List[Optional[int]],
        p: int,
        q: int,
        expected: int,
    ) -> None:
        root = bst.build_tree(tree_nodes)
        assert root, "root must not be None!"
        p_node = find_node(root, p)
        q_node = find_node(root, q)
        assert p_node and q_node, f"{p} and {q} must both be found in root!"

        r = func(root, p_node, q_node)
        if r and r.val == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Lowest common ancestor in {tree_nodes} for {p} and {q} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Lowest common ancestor in {tree_nodes} for {p} and {q} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.lowestCommonAncestor_recursive, tree_nodes, p, q, expected)
    test_impl(sln.lowestCommonAncestor_recursive_fast, tree_nodes, p, q, expected)


if __name__ == "__main__":
    test_solution(
        tree_nodes=[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], p=5, q=1, expected=3
    )
    test_solution(
        tree_nodes=[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], p=5, q=4, expected=5
    )
    test_solution(tree_nodes=[1, 2], p=1, q=2, expected=1)
