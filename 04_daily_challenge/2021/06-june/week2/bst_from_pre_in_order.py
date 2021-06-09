# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3772/

# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.

# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,None,None,15,7]

# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Constraints:
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

from typing import Callable, List, Optional
from termcolor import colored
from shared import bst

TreeNode = bst.TreeNode


class Solution:
    def buildTree_recursive(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        preorder_index = 0
        inorder_index_map = {v: i for i, v in enumerate(inorder)}

        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_index, inorder_index_map
            if left > right:
                return None
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)
            preorder_index += 1
            root.left = array_to_tree(left, inorder_index_map[root_val] - 1)
            root.right = array_to_tree(inorder_index_map[root_val] + 1, right)
            return root

        return array_to_tree(0, len(preorder) - 1)


SolutionFunc = Callable[[List[int], List[int]], Optional[TreeNode]]


def test_solution(
    preorder: List[int], inorder: List[int], expected: List[Optional[int]]
) -> None:
    def test_impl(
        func: SolutionFunc,
        preorder: List[int],
        inorder: List[int],
        expected: List[Optional[int]],
    ) -> None:
        r = func(preorder, inorder)
        r_list = bst.build_list(r)
        e_list = bst.build_list(bst.build_tree(expected))
        if r_list == e_list:
            print(
                colored(
                    f"PASSED {func.__name__} => BST from preorder: {preorder} and inorder: {inorder} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => BST from preorder: {preorder} and inorder: {inorder} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.buildTree_recursive, preorder, inorder, expected)


if __name__ == "__main__":
    test_solution(
        preorder=[3, 9, 20, 15, 7],
        inorder=[9, 3, 15, 20, 7],
        expected=[3, 9, 20, None, None, 15, 7],
    )

    test_solution(
        preorder=[-1],
        inorder=[-1],
        expected=[-1],
    )
