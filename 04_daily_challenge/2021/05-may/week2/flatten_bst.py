# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3742/

# Flatten Binary Tree to Linked List
# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child
# pointer points to the next node in the list and the left child pointer is
# always None.

# The "linked list" should be in the same order as a pre-order traversal of the
# binary tree.

# Example 1:
# Input: root = [1,2,5,3,4,None,6]
# Output: [1,None,2,None,3,None,4,None,5,None,6]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [0]
# Output: [0]

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

# Follow up: Can you flatten the tree in-place (with O(1) extra space)?

from typing import Callable, List, Optional
from shared import bst
from termcolor import colored

TreeNode = bst.TreeNode
NodeList = List[Optional[int]]


class Solution:
    def flatten(self, root: TreeNode) -> None:
        return self.flatten_reversed_postorder_traversal(root)

    # https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37154/8-lines-of-python-solution-(reverse-preorder-traversal)
    def flatten_reversed_postorder_traversal(self, root: Optional[TreeNode]) -> None:
        prev: Optional[TreeNode] = None

        def traverse(node: Optional[TreeNode]) -> None:
            if not node:
                return None

            nonlocal prev

            traverse(node.right)
            traverse(node.left)

            node.right = prev
            node.left = None
            prev = node

        traverse(root)

    # https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37010/Share-my-simple-NON-recursive-solution-O(1)-space-complexity!
    def flatten_iterative_morris(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None

        now: Optional[TreeNode] = root

        while now:
            if now.left:
                pre = now.left
                while pre.right:
                    pre = pre.right
                pre.right = now.right
                now.right = now.left
                now.left = None

            now = now.right


SolutionFunc = Callable[[Optional[TreeNode]], None]


def test_solution(nodes: NodeList, expected: NodeList) -> None:
    def test_impl(func: SolutionFunc, nodes: NodeList, expected: NodeList) -> None:
        root = bst.build_tree(nodes)
        func(root)
        r = bst.build_list(root)
        e = bst.build_list(bst.build_tree(expected))
        if r == e:
            print(
                colored(f"PASSED {func.__name__} => {nodes} flattened to {r}", "green")
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {nodes} flattened to {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.flatten_reversed_postorder_traversal, nodes, expected)
    test_impl(sln.flatten_iterative_morris, nodes, expected)


if __name__ == "__main__":
    test_solution(
        nodes=[1, 2, 5, 3, 4, None, 6],
        expected=[1, None, 2, None, 3, None, 4, None, 5, None, 6],
    )
    test_solution(nodes=[], expected=[])
    test_solution(nodes=[0], expected=[0])
