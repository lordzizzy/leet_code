# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3626/

# Trim a Binary Search Tree

# Given the root of a binary search tree and the lowest and highest boundaries
# as low and high, trim the tree so that all its elements lies in [low, high].

# Trimming the tree should not change the relative structure of the elements
# that will remain in the tree (i.e., any node's descendant should remain a
# descendant). It can be proven that there is a unique answer.

# Return the root of the trimmed binary search tree. Note that the root may
# change depending on the given bounds.

# Example 1:
# Input: root = [1,0,2], low = 1, high = 2
# Output: [1,null,2]

# Example 2:
# Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
# Output: [3,2,null,1]

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
# The number of nodes in the tree in the range [1, 10⁴].
# 0 <= Node.val <= 10⁴
# The value of each node in the tree is unique.
# root is guaranteed to be a valid binary search tree.
# 0 <= low <= high <= 10⁴


from termcolor import colored
from typing import Callable, List, Optional
from shared import bst

TreeNode = bst.TreeNode


class Solution:
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        return self.trimBST_iterative(root, low, high)
        # return self.trimBST_recursive(root, low, high)

    def trimBST_recursive(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        def trim(node: Optional[TreeNode]) -> Optional[TreeNode]:
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

    def trimBST_iterative(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        # find real root to return
        while root and not (low <= root.val <= high):
            if root.val > high:
                root = root.left
            elif root.val < low:
                root = root.right

        stack: List[Optional[TreeNode]] = [root]
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


SolutionFunc = Callable[[Optional[TreeNode], int, int], Optional[TreeNode]]


def test_solution(
    nodes: List[Optional[int]], low: int, high: int, expected: List[Optional[int]]
):
    def test_impl(
        func: SolutionFunc,
        nodes: List[Optional[int]],
        low: int,
        high: int,
        expected: List[Optional[int]],
    ) -> Optional[TreeNode]:

        root = bst.build_tree(nodes)
        root = func(root, low, high)
        r = bst.build_list(root)
        if r == bst.build_list(bst.build_tree(expected)):
            print(
                colored(
                    f"PASSED {func.__name__}=> binary tree of {nodes} with range min={low}, max={high} trimmed is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__}=> binary tree of {nodes} with range min={low}, max={high} trimmed is {r}, expected; {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.trimBST_iterative, nodes, low, high, expected)
    test_impl(sln.trimBST_recursive, nodes, low, high, expected)


if __name__ == "__main__":
    test_solution(
        nodes=[3, 0, 4, None, 2, None, None, 1], low=1, high=3, expected=[3, 2, None, 1]
    )
    test_solution(nodes=[3, 2, 4, 1], low=1, high=1, expected=[1])
    test_solution(nodes=[1], low=1, high=2, expected=[1])
    test_solution(nodes=[1, None, 2], low=1, high=3, expected=[1, None, 2])
    test_solution(nodes=[1, None, 2], low=2, high=4, expected=[2])
