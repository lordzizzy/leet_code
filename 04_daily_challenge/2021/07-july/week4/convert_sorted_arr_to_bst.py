# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3827/

# Convert Sorted Array to Binary Search Tree

# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which the depth of the two
# subtrees of every node never differs by more than one.

# Example 1:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

# Constraints:

# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in a strictly increasing order.

from typing import Callable, List, Optional, Tuple

from shared import bst
from termcolor import colored

TreeNode = bst.TreeNode


class Solution:
    def sortedArrayToBST_recursive(self, nums: List[int]) -> Optional[TreeNode]:
        def convert(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(val=nums[mid])
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)
            return node

        return convert(0, len(nums) - 1)

    def sortedArrayToBST_iterative(self, nums: List[int]) -> Optional[TreeNode]:
        root = None
        stack: List[Tuple[Optional[TreeNode], int, int, int]] = [
            (root, 0, 0, len(nums) - 1)
        ]

        while stack:
            node, cmd, left, right = stack.pop()
            if left > right:
                if cmd == 1:
                    node.left = None
                elif cmd == 2:
                    node.right = None
                continue

            mid = (left + right) // 2
            new = TreeNode(val=nums[mid])
            if cmd == 0:
                root = new
            elif cmd == 1:
                node.left = new
            elif cmd == 2:
                node.right = new

            # push right then left, as we are doing preorder traversal (left
            # will be popped first)
            stack.append((new, 2, mid + 1, right))
            stack.append((new, 1, left, mid - 1))

        return root


PossibleResults = List[List[Optional[int]]]
SolutionFunc = Callable[[List[int]], Optional[TreeNode]]


def test_solution(nums: List[int], possible_results: PossibleResults) -> None:
    def test_impl(
        func: SolutionFunc, nums: List[int], possible_results: PossibleResults
    ) -> None:
        res = func(nums)
        res_list = bst.build_list(res)
        if any(
            res_list == bst.build_list(bst.build_tree(exp)) for exp in possible_results
        ):
            print(
                colored(
                    f"PASSED {func.__name__} => Sorted array {nums} to height-balanced BST is {res_list}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Sorted array {nums} to height-balanced BST is {res_list} but expected any from {possible_results}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.sortedArrayToBST_recursive, nums, possible_results)
    test_impl(sln.sortedArrayToBST_iterative, nums, possible_results)


def main():
    test_solution(
        nums=[-10, -3, 0, 5, 9],
        possible_results=[[0, -3, 9, -10, None, 5], [0, -10, 5, None, -3, None, 9]],
    )
    test_solution(nums=[1, 3], possible_results=[[3, None, 1], [1, None, 3]])


if __name__ == "__main__":
    main()
