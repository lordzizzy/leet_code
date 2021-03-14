# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3671/

# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node
# from the beginning and the kth node from the end (the list is 1-indexed).

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]

# Example 3:
# Input: head = [1], k = 1
# Output: [1]

# Example 4:
# Input: head = [1,2], k = 1
# Output: [2,1]

# Example 5:
# Input: head = [1,2,3], k = 2
# Output: [1,2,3]


# Constraints:
# The number of nodes in the list is n.
# 1 <= k <= n <= 10⁵
# 0 <= Node.val <= 100

from typing import Callable, List, Optional
from termcolor import colored
from shared.linked_list import ListNode, build_linked_list, build_node_data_list


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return self.swapNodes_only_values(head, k)

    def swapNodes_only_values(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        walker = runner = head
        for _ in range(k - 1):
            runner = runner.next
        first, runner = runner, runner.next
        while runner:
            walker = walker.next
            runner = runner.next
        walker.val, first.val = first.val, walker.val
        return head

    def swapNodes_only_values_list(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        if head is None:
            return None
        nodes = [head]
        cur = head
        while cur:
            cur = cur.next
            if cur:
                nodes.append(cur)
        n1, n2 = nodes[k - 1], nodes[-k]
        n1.val, n2.val = n2.val, n1.val
        return head

    def swapNodes_2ptrs(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        walker = runner = first = dummy
        for _ in range(k):
            first = runner
            runner = runner.next
        while runner.next:
            walker = walker.next
            runner = runner.next
        left, right = first.next, walker.next
        if right.next is left:
            left, right = right, left
            first, walker = walker, first
        left_next, right_next = left.next, right.next
        if left_next is right:
            first.next = right
            right.next = left
            left.next = right_next
        else:
            first.next, walker.next = right, left
            right.next, left.next = left_next, right_next
        return dummy.next

    # todo
    def swapNodes_list(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # lst: List[ListNode] = []
        # curr = head
        # while curr:
        #     lst.append(curr)
        #     curr = curr.next
        # i = k - 1
        # if lst[i] is not lst[-k]:
        #     if len(lst) == 2:
        #         lst[0].next = None
        #         lst[1].next = lst[0]
        #         return lst[1]

        #     lst[i - 1].next = lst[-k]
        #     tmp = lst[i].next
        #     lst[i].next = lst[-k].next
        #     lst[-k].next = tmp
        #     lst[-(k + 1)].next = lst[i]

        # return lst[0]
        raise NotImplementedError()


NodeDataList = List[int]
SolutionFunc = Callable[[Optional[ListNode], int], Optional[ListNode]]


def test_solution(nodes: NodeDataList, k: int, expected: NodeDataList) -> None:
    def test_impl(
        func: SolutionFunc, nodes: NodeDataList, k: int, expected: NodeDataList
    ) -> None:
        head = build_linked_list(nodes)
        r = func(head, k)
        r_nodes = build_node_data_list(r)
        if r_nodes == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {nodes} swapped at {k}th element from the beginning and the {k}th node from the end is {r_nodes}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"PASSED {func.__name__} => {nodes} swapped at {k}th element from the beginning and the {k}th node from the end is {r_nodes} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.swapNodes_only_values, nodes, k, expected)
    test_impl(sln.swapNodes_only_values_list, nodes, k, expected)
    test_impl(sln.swapNodes_2ptrs, nodes, k, expected)


if __name__ == "__main__":
    test_solution(nodes=[1, 2, 3, 4, 5], k=2, expected=[1, 4, 3, 2, 5])
    test_solution(
        nodes=[7, 9, 6, 6, 7, 8, 3, 0, 9, 5],
        k=5,
        expected=[7, 9, 6, 6, 8, 7, 3, 0, 9, 5],
    )
    test_solution(nodes=[1], k=1, expected=[1])
    test_solution(nodes=[1, 2], k=1, expected=[2, 1])
    test_solution(nodes=[1, 2, 3], k=2, expected=[1, 2, 3])
