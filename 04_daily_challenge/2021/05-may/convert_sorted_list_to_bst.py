# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3733/

# Given the head of a singly linked list where elements are sorted in ascending
# order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.

# Example 1:
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the
# shown height balanced BST.

# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [0]
# Output: [0]

# Example 4:
# Input: head = [1,3]
# Output: [3,1]

# Constraints:
# The number of nodes in head is in the range [0, 2 * 10⁴].
# -10⁵ <= Node.val <= 10⁵

from typing import Callable, List, Optional
from termcolor import colored

from shared import linked_list
from shared import bst

ListNode = linked_list.ListNode
TreeNode = bst.TreeNode

ListNodeDataList = linked_list.NodeDataList
TreeNodeDataList = List[Optional[int]]


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        # find middle point
        slow = head
        fast = head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # tmp points to root
        tmp = slow.next
        # separate left child
        slow.next = None
        # build tree
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root


SolutionFunc = Callable[[Optional[ListNode]], Optional[TreeNode]]


def test_solution(nodes: ListNodeDataList, expected: TreeNodeDataList) -> None:
    def test_impl(
        func: SolutionFunc, nodes: ListNodeDataList, expected: TreeNodeDataList
    ) -> None:
        head = linked_list.build_linked_list(nodes)
        root = func(head)
        bst_nodes = bst.build_list(root)
        exp_nodes = bst.build_list(bst.build_tree(expected))
        if bst_nodes == exp_nodes:
            print(
                colored(
                    f"PASSED {func.__name__} => {nodes} converted to BST: {bst_nodes}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {nodes} converted to BST: {bst_nodes} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.sortedListToBST, nodes, expected)


if __name__ == "__main__":
    test_solution(nodes=[-10, -3, 0, 5, 9], expected=[0, -3, 9, -10, None, 5])
    test_solution(nodes=[], expected=[])
    test_solution(nodes=[0], expected=[0])
    test_solution(nodes=[1, 3], expected=[3, 1])
