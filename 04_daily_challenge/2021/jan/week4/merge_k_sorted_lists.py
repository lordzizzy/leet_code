# Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []

# Constraints:
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.

from typing import List

from termcolor import colored


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        head = lists[0]
        for i in range(1, len(lists)):
            head = self.merge2Lists(head, lists[i])
        return head

    def merge2Lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        head = l1 if l1.val <= l2.val else l2
        head.next = self.merge2Lists(
            l1.next, l2) if l1.val <= l2.val else self.merge2Lists(l1, l2.next)
        return head


def toListOfListNodes(input: List[List[int]]) -> List[ListNode]:
    if not input or len(input) == 0:
        return None

    result = []
    for lst in input:
        if not lst or len(lst) == 0:
            continue
        head = ListNode(val=lst[0], next=None)
        curr = head
        for i in range(1, len(lst)):
            node = ListNode(val=lst[i], next=None)
            curr.next = node
            curr = node
        result.append(head)

    return result


def toListOfNums(nodes: List[ListNode]) -> List[List[int]]:
    result = []
    for node in nodes:
        nums = []
        while node:
            nums.append(node.val)
            node = node.next
        result.append(nums)
    return result


def toListOfNums(node: ListNode) -> List[int]:
    nums = []
    while node:
        nums.append(node.val)
        node = node.next
    return nums


def test_toListOfListNodes(lists: List[List[int]]):
    nodes = toListOfListNodes(lists)
    if toListOfNums(nodes) == lists:
        print(colored(f"PASSED.", "green"))
    else:
        print(colored(f"FAILED.", "red"))


def test_Solution(input: List[List[int]], expected: List[int]):
    # convert input into List of ListNodes
    sln = Solution()
    r = sln.mergeKLists(toListOfListNodes(input))
    if toListOfNums(r) == expected:
        print(colored(f"PASSED - merged {input} into {r}", "green"))
    else:
        print(
            colored(f"FAILED - merged {input} into {r}, but expected: {expected}", "red"))


if __name__ == "__main__":
    test_Solution(input=[[1, 4, 5], [1, 3, 4], [2, 6]],
                  expected=[1, 1, 2, 3, 4, 4, 5, 6])
