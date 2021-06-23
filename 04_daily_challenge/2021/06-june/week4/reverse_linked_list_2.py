# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3789/

# Reverse Linked List II
# Given the head of a singly linked list and two integers left and right where
# left <= right, reverse the nodes of the list from position left to position
# right, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [5], left = 1, right = 1
# Output: [5]

# Constraints:

# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n

# Follow up: Could you do it in one pass?

from typing import Callable, List

from shared import linked_list
from termcolor import colored

ListNode = linked_list.ListNode


class Solution:
    # reference
    # https://leetcode.com/problems/reverse-linked-list-ii/discuss/30709/Talk-is-cheap-show-me-the-code-(and-DRAWING)
    #
    def reverseBetween_iterative(
        self, head: ListNode, left: int, right: int
    ) -> ListNode:
        if left == right:
            return head

        p = dummy = ListNode(val=0)
        dummy.next = head

        for _ in range(left - 1):
            p = p.next
        tail = p.next

        for _ in range(right - left):
            tmp = p.next
            p.next = tail.next
            tail.next = tail.next.next
            p.next.next = tmp

        return dummy.next

    def reverseBetween_iterative_2(
        self, head: ListNode, left: int, right: int
    ) -> ListNode:
        m, n = left, right
        dummy = ListNode(val=0)
        dummy.next = head

        while m > 1:
            dummy = dummy.next
            m -= 1
        r = head

        while n > 0:
            r = r.next
            n -= 1

        prev, curr = dummy, dummy.next
        while curr != r:
            curr.next, prev, curr = prev, curr, curr.next

        dummy.next.next = curr
        if dummy.next == head:
            head = prev
        dummy.next = prev

        return head


SolutionFunc = Callable[[ListNode, int, int], ListNode]


def test_solution(
    head_nodes: List[int], left: int, right: int, expected: List[int]
) -> None:
    def test_impl(
        func: SolutionFunc,
        head_nodes: List[int],
        left: int,
        right: int,
        expected: List[int],
    ) -> None:
        assert head_nodes, f"Head data list cannot be None"
        head = linked_list.build_linked_list(head_nodes)
        assert head, f"Head cannot be None"

        r = func(head, left, right)
        r_nodes = linked_list.build_node_data_list(r)
        if r_nodes == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Reverse linked list {head_nodes} from left-node({left}) to right-node({right}) is {r_nodes}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Reverse linked list {head_nodes} from left-node({left}) to right-node({right}) is {r_nodes} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.reverseBetween_iterative, head_nodes, left, right, expected)
    test_impl(sln.reverseBetween_iterative_2, head_nodes, left, right, expected)


if __name__ == "__main__":
    test_solution(head_nodes=[1, 2, 3, 4, 5], left=2, right=4, expected=[1, 4, 3, 2, 5])
    test_solution(head_nodes=[5], left=1, right=1, expected=[5])
    test_solution(
        head_nodes=[10, 3, 2, 8, 6], left=2, right=5, expected=[10, 6, 8, 2, 3]
    )
