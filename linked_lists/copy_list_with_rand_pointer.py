# https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3635/

# Copy List with Random Pointer
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or None.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or None if it does not point to any node.
# Your code will only be given the head of the original linked list.

# Example 1:
# Input: head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,None],[13,0],[11,4],[10,2],[1,0]]

# Example 2:
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Example 3:
# Input: head = [[3,None],[3,0],[3,None]]
# Output: [[3,None],[3,0],[3,None]]

# Example 4:
# Input: head = []
# Output: []
# Explanation: The given linked list is empty (None pointer), so return None.

# Constraints:
# 0 <= n <= 1000
# -10000 <= Node.val <= 10000
# Node.random is None or is pointing to some node in the linked list.


from typing import DefaultDict, Optional, List
from termcolor import colored

from shared.linked_list_rand import ListNode, NodeList, build_linked_list, build_node_list


class Solution:
    def copyRandomList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.copyRandomList_dict_lookup(head)

    # https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43485/Clear-and-short-python-O(2n)-and-O(n)-solution
    def copyRandomList_dict_lookup(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if head is None:
            return None

        lookup = DefaultDict[Optional[ListNode], Optional[ListNode]](
            lambda: ListNode(0)
        )
        lookup[None] = None
        old = head

        while old:
            lookup[old].val = old.val
            lookup[old].next = lookup[old.next]
            lookup[old].random = lookup[old.random]
            old = old.next

        return lookup[head]

    def copyRandomList_arr_lookup(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        nodes: List[ListNode] = []
        new_nodes: List[ListNode] = []

        while head:
            nodes.append(head)
            new_nodes.append(ListNode(head.val))
            head = head.next

        n = len(new_nodes)

        for i, new in enumerate(new_nodes):
            new.next = new_nodes[i + 1] if i < n - 1 else None
            rand_node = nodes[i].random
            if rand_node is not None:
                rand_idx = nodes.index(rand_node)
                new.random = new_nodes[rand_idx]

        return new_nodes[0]


def test_solution(nodes: NodeList, expected: NodeList):
    sln = Solution()
    head = build_linked_list(nodes)
    r = sln.copyRandomList(head)
    r_nodes = build_node_list(r)
    res = len(r_nodes) == len(expected)
    for i in range(len(r_nodes)):
        if r_nodes[i] != expected[i]:
            res = False
            break

    if res:
        print(colored(f"PASSED => copied list {nodes} with result: {r_nodes}", "green"))
    else:
        print(
            colored(
                f"FAILED => copied list {nodes} with result: {r_nodes}, but expected {expected}",
                "red",
            )
        )


if __name__ == "__main__":

    test_solution(
        nodes=[[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
        expected=[[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
    )

    test_solution(
        nodes=[[1, 1], [2, 1]],
        expected=[[1, 1], [2, 1]],
    )

    test_solution(
        nodes=[[3, None], [3, 0], [3, None]],
        expected=[[3, None], [3, 0], [3, None]],
    )

    test_solution(
        nodes=[],
        expected=[],
    )