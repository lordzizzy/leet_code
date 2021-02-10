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

from __future__ import annotations
from typing import DefaultDict, Optional, List
from termcolor import colored

# Definition for a Node.
class Node:
    def __init__(
        self, x: int, next: Optional[Node] = None, random: Optional[Node] = None
    ):
        self.val = x
        self.next = next
        self.random = random

    def __repr__(self) -> str:
        res = ""
        head = self
        while head:
            if head.next:
                res += f"(val:{head.val}, rand:{id(head.random) if head.random else None})-->"
            else:
                res += f"(val:{head.val}, rand:{id(head.random) if head.random else None})-->None"
            head = head.next
        return res


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        return self.copyRandomList_dict_lookup(head)

    def copyRandomList_dict_lookup(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None

        lookup = DefaultDict[Optional[Node], Optional[Node]](lambda: Node(0))
        lookup[None] = None
        old = head

        while old:
            lookup[old].val = old.val
            lookup[old].next = lookup[old.next]
            lookup[old].random = lookup[old.random]
            old = old.next

        return lookup[head]

    def copyRandomList_arr_lookup(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None

        nodes: List[Node] = []
        new_nodes: List[Node] = []

        while head:
            nodes.append(head)
            new_nodes.append(Node(head.val))
            head = head.next

        n = len(new_nodes)

        for i, new in enumerate(new_nodes):
            new.next = new_nodes[i + 1] if i < n - 1 else None
            rand_node = nodes[i].random
            if rand_node is not None:
                rand_idx = nodes.index(rand_node)
                new.random = new_nodes[rand_idx]

        return new_nodes[0]


NodeData = List[Optional[int]]
NodeList = List[NodeData]


def build_linked_list(nodes: NodeList) -> Optional[Node]:
    n = len(nodes)
    if n == 0:
        return None
    linked_list_nodes: List[Node] = []
    # create linked list node and populate values
    for data in nodes:
        val = data[0]
        if val is None:
            raise TypeError()
        node = Node(val)
        linked_list_nodes.append(node)
    # set next and random links foreach linked list node
    for i, ll_node in enumerate(linked_list_nodes):
        data = nodes[i]
        rand_idx = data[1]
        ll_node.random = linked_list_nodes[rand_idx] if rand_idx is not None else None
        ll_node.next = linked_list_nodes[i + 1] if i + 1 < n else None

    return linked_list_nodes[0]


def build_node_list(head: Optional[Node]) -> NodeList:
    if head is None:
        return []
    nodes: NodeList = []
    ll_nodes: List[Node] = []
    # create node data while traversing through head
    while head:
        node_data = [head.val, None]
        nodes.append(node_data)
        ll_nodes.append(head)
        head = head.next
    # populate node.random field once we have all the nodes relative index
    for i, node in enumerate(nodes):
        ll_node = ll_nodes[i]
        node[0] = ll_node.val
        node[1] = ll_nodes.index(ll_node.random) if ll_node.random is not None else None

    return nodes


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