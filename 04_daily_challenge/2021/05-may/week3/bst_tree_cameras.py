# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3745/

# Binary Tree Cameras
# Given a binary tree, we install cameras on the nodes of the tree.

# Each camera at a node can monitor its parent, itself, and its immediate
# children.

# Calculate the minimum number of cameras needed to monitor all nodes of the
# tree.

# Example 1:
# Input: [0,0,None,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.

# Example 2:
# Input: [0,0,None,0,None,0,None,None,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the
# tree. The above image shows one of the valid configurations of camera
# placement.


# Note:
# The number of nodes in the given tree will be in the range [1, 1000].
# Every node has value 0.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Callable, List, Optional, Tuple
from termcolor import colored
from shared import bst


TreeNode = bst.TreeNode
NodeList = List[Optional[int]]


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        return self.minCameraCover_greedy_dfs(root)

    # https://leetcode.com/problems/binary-tree-cameras/discuss/211180/JavaC%2B%2BPython-Greedy-DFS
    def minCameraCover_greedy_dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        HAS_CAM, COVERED, NOT_COVERED = 0, 1, 2
        cnt = 0

        def cover(node: Optional[TreeNode]) -> int:
            nonlocal cnt

            if not node:
                return COVERED

            l = cover(node.left)
            r = cover(node.right)

            if l == NOT_COVERED or r == NOT_COVERED:
                cnt += 1
                return HAS_CAM

            if l == HAS_CAM or r == HAS_CAM:
                return COVERED

            return NOT_COVERED

        return cnt + 1 if cover(root) == NOT_COVERED else cnt

    def minCameraCover_dp(self, root: Optional[TreeNode]) -> int:
        MAX_NODES = 1000

        def solve(node: Optional[TreeNode]) -> Tuple[int, int, int]:
            # 0: Strict ST; All nodes below this are covered, but not this one
            # 1: Normal ST; All nodes below and incl this are covered - no camera
            # 2: Placed camera; All nodes below this are covered, plus camera here

            if not node:
                return 0, 0, MAX_NODES

            L = solve(node.left)
            R = solve(node.right)

            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            dp2 = 1 + min(L) + min(R)

            return dp0, dp1, dp2

        return min(solve(root)[1:])


SolutionFunc = Callable[[Optional[TreeNode]], int]


def test_solution(nodes: NodeList, expected: int) -> None:
    def test_impl(func: SolutionFunc, nodes: NodeList, expected: int) -> None:
        root = bst.build_tree(nodes)
        r = func(root)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Min cameras to place in {nodes} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Min cameras to place in {nodes} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.minCameraCover_greedy_dfs, nodes, expected)
    test_impl(sln.minCameraCover_dp, nodes, expected)


if __name__ == "__main__":
    test_solution(nodes=[0, 0, None, 0, 0], expected=1)
    test_solution(nodes=[0, 0, None, 0, None, 0, None, None, 0], expected=2)
    test_solution(nodes=[], expected=0)
    test_solution(nodes=[0], expected=1)
