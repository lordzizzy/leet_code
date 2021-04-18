# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3712/

# Given the head of a linked list, remove the nth node from the end of the list
# and return its head.

# Follow up: Could you do this in one pass?

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

from typing import Callable, List, Optional
from shared import linked_list
from termcolor import colored

ListNode = linked_list.ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> Optional[ListNode]:
        return self.removeNthFromEnd_2pass(head, n)

    def removeNthFromEnd_2pass(self, head: ListNode, n: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        # find size of list
        first = head
        size = 0
        while first:
            size += 1
            first = first.next
        # goto size - n node from dummy and remove from there
        size -= n
        first = dummy
        while size > 0:
            size -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next

    # 12 ms solution
    def removeNthFromEnd_slow_fast_ptr(
        self, head: ListNode, n: int
    ) -> Optional[ListNode]:
        slow = fast = head

        for _ in range(n):
            fast = fast.next
        if fast is None:
            return head.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head


SolutionFunc = Callable[[ListNode, int], Optional[ListNode]]


def test_solution(head_list: List[int], n: int, expected: List[int]) -> None:
    def test_impl(
        func: SolutionFunc, head_list: List[int], n: int, expected: List[int]
    ) -> None:
        head = linked_list.build_linked_list(head_list)
        assert head, f"head cannot be null"
        r = func(head, n)
        r_list = linked_list.build_node_data_list(r)
        if r_list == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Result of removing {n}th node from end of {head_list} is {r_list}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Result of removing {n}th node from end of {head_list} is {r_list} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    # test_impl(sln.removeNthFromEnd, head_list, n, expected)
    test_impl(sln.removeNthFromEnd_slow_fast_ptr, head_list, n, expected)


if __name__ == "__main__":
    # test_solution(head_list=[1, 2, 3, 4, 5], n=2, expected=[1, 2, 3, 5])
    test_solution(head_list=[1, 2], n=2, expected=[2])
    
