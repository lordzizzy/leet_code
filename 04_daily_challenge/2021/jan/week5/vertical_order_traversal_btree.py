# https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/583/week-5-january-29th-january-31st/3621/

# Vertical order traversal of a binary tree

# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

# For each node at position (x, y), its left and right children will be at positions (x - 1, y - 1) and (x + 1, y - 1) respectively.

# The vertical order traversal of a binary tree is a list of non-empty reports for each unique x-coordinate from left to right. Each report is a list of all nodes at a given x-coordinate. The report should be primarily sorted by y-coordinate from highest y-coordinate to lowest. If any two nodes have the same y-coordinate in the report, the node with the smaller value should appear earlier.

# Return the vertical order traversal of the binary tree.

# Example 1:
# Input: root = [3,9,20,None,None,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation: Without loss of generality, we can assume the root node is at position (0, 0):
# The node with value 9 occurs at position (-1, -1).
# The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2).
# The node with value 20 occurs at position (1, -1).
# The node with value 7 occurs at position (2, -2).
# Example 2:


# Input: root = [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation: The node with value 5 and the node with value 6 have the same position according to the given scheme.
# However, in the report [1,5,6], the node with value 5 comes first since 5 is smaller than 6.


# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 1000

# sample 24 ms solution
# class Solution:
#     def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
#         grid = {}
#         queue = [(root, 0, 0)]
#         res = []
#         for cur in queue:
#             if cur[0]:
#                 horizon, lvl = cur[1], cur[2]
#                 if not cur[1] in grid:
#                     grid[cur[1]]=[[lvl, cur[0].val]]
#                 else:
#                     grid[cur[1]].append([lvl, cur[0].val])
#                 queue.append((cur[0].left, horizon-1, lvl+1))
#                 queue.append((cur[0].right, horizon+1, lvl+1))
#         for i in sorted(grid.keys()):
#             # print("i:",i)
#             # print("grid[i]:",grid[i])
#             res.append([value[1] for value in sorted(grid[i])])
#         return res

from collections import deque
from typing import DefaultDict, List
from termcolor import colored

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"<{self.val} {self.left}, {self.right}>"


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def visit(root: TreeNode, dic, x, y):

            if root.left:
                visit(root.left, dic, x-1, y+1)

            l = dic.get(x)
            if not l:
                l = []
                dic[x] = l
            l.append((y, root.val))

            if root.right:
                visit(root.right, dic, x+1, y+1)

        dic = DefaultDict()
        visit(root, dic, 0, 0)
        tree_lst = []
        for x in sorted(dic.keys()):
            print(x)
            d = dic[x]
            d.sort()
            l = []
            for y, val in d:
                l.append(val)
            tree_lst.append(l)
        return tree_lst


def build_tree(nodes) -> TreeNode:
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


def test_solution(nodes, expected: List[List[int]]):
    root = build_tree(nodes)
    sln = Solution()
    r = sln.verticalTraversal(root)
    success = len(r) == len(expected)
    if success:
        for i in range(0, len(r)):
            l1 = r[i]
            l2 = expected[i]
            if l1 != l2:
                success = False
                break
    if success:
        print(
            colored(f"PASSED => vertical travesal of {nodes} is {r}", "green"))
    else:
        print(colored(
            f"FAILED => vertical travesal of {nodes} is {r}, but expected: {expected}", "red"))


if __name__ == "__main__":
    test_solution(nodes=[3, 9, 20, None, None, 15, 7],
                  expected=[[9], [3, 15], [20], [7]])

    test_solution(nodes=[1, 2, 3, 4, 5, 6, 7],
                  expected=[[4], [2], [1, 5, 6], [3], [7]])

    test_solution(nodes=[3, 1, 4, 0, 2, 2],
                  expected=[[0], [1], [3, 2, 2], [4]])

    test_solution(nodes=[0, 10, 1, None, None, 2, 4, 3, 5, None, None, 6, None, 7, 9, 8, None, None, None, None, 11, None, None, 12],
                  expected=[[8], [6], [10, 3], [0, 2, 7], [1, 5], [4, 9, 12], [11]])
