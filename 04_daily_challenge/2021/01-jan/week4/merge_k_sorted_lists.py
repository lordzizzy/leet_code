# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3615/

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

from typing import List, Optional
from termcolor import colored
from shared.linked_list import ListNode


ListNodeList = List[Optional[ListNode]]


class Solution:
    def mergeKLists(self, lists: ListNodeList) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        # n log K time complexity
        while len(lists) > 1:
            merged: ListNodeList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged.append(self.merge2Lists(l1, l2))

            lists = merged

        return lists[0]

    def merge2Lists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(val=0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next


def build_listnode_list(input: List[List[int]]) -> ListNodeList:
    if not input or len(input) == 0:
        return []

    result: ListNodeList = []
    for lst in input:
        if not lst or len(lst) == 0:
            continue
        head = ListNode(val=lst[0])
        curr = head
        for i in range(1, len(lst)):
            node = ListNode(val=lst[i])
            curr.next = node
            curr = node
        result.append(head)

    return result


def build_listnode_nums(node: Optional[ListNode]) -> List[Optional[int]]:
    nums: List[Optional[int]] = []
    while node:
        nums.append(node.val)
        node = node.next
    return nums


def test_Solution(input: List[List[int]], expected: List[int]):
    sln = Solution()
    lists = build_listnode_list(input)
    r = sln.mergeKLists(lists)
    if build_listnode_nums(r) == expected:
        print(colored(f"PASSED - merged {input} into {r}", "green"))
    else:
        print(
            colored(
                f"FAILED - merged {input} into {r}, but expected: {expected}", "red"
            )
        )


if __name__ == "__main__":
    test_Solution(
        input=[[1, 4, 5], [1, 3, 4], [2, 6]], expected=[1, 1, 2, 3, 4, 4, 5, 6]
    )
