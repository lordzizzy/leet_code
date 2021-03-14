# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3627/

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Constraints:
# The number of the nodes in the list is in the range [0, 104].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.


# Follow up: Can you solve it using O(1) (i.e. constant) memory?

from __future__ import annotations
from typing import Callable, List, Optional
from termcolor import colored

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int, next: Optional[ListNode] = None):
        self.val = x
        self.next = next

    def __str__(self) -> str:
        s: str = ""
        curr = self
        visited = set()
        while curr:
            if curr in visited:
                s = s + f"cycle to {curr.next.val}" if curr.next else s
                break
            visited.add(curr)
            if curr.next:
                s = s + f"{curr.val}->"
                curr = curr.next
            else:
                s = s + f"{curr.val}"
                break
        return s


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        return self.hasCycle_floyd_algo(head)

    def hasCycle_set_lookup(self, head: Optional[ListNode]) -> bool:
        lookup = set()
        while head:
            if head in lookup:
                return True
            lookup.add(head)
            head = head.next
        return False

    def hasCycle_floyd_algo(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast and slow and fast.val == slow.val:
                return True
        return False


def build_linked_list(nodes: List[int], pos: int) -> ListNode:
    stack: List[ListNode] = []
    prev = None
    for v in nodes:
        node = ListNode(v)
        if prev:
            prev.next = node
        prev = node
        stack.append(node)

    if stack and 0 <= pos < len(nodes):
        stack[-1].next = stack[pos]

    return stack[0]


SolutionFunc = Callable[[ListNode], bool]


def test_solution(nodes: List[int], pos: int, expected: bool):
    def test_impl(func: SolutionFunc, nodes: List[int], pos: int, expected: bool):
        head = build_linked_list(nodes, pos)
        r = func(head)
        if r == expected:
            print(
                colored(f"PASSED {func.__name__}=> {nodes} has cycle is {r}", "green")
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__}=> {nodes} has cycle is {r}, but expected: {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.hasCycle_floyd_algo, nodes, pos, expected)
    test_impl(sln.hasCycle_set_lookup, nodes, pos, expected)


if __name__ == "__main__":
    test_solution(nodes=[3, 2, 0, -4], pos=1, expected=True)
    test_solution(nodes=[1, 2], pos=0, expected=True)
    test_solution(nodes=[1], pos=-1, expected=False)
