from __future__ import annotations
from typing import Optional, List


class ListNode:
    def __init__(
        self, x: int, next: Optional[ListNode] = None, random: Optional[ListNode] = None
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


NodeData = List[Optional[int]]
NodeList = List[NodeData]


def build_linked_list(nodes: NodeList) -> Optional[ListNode]:
    n = len(nodes)
    if n == 0:
        return None
    linked_list_nodes: List[ListNode] = []
    # create linked list node and populate values
    for data in nodes:
        val = data[0]
        if val is None:
            raise TypeError()
        node = ListNode(val)
        linked_list_nodes.append(node)
    # set next and random links foreach linked list node
    for i, ll_node in enumerate(linked_list_nodes):
        data = nodes[i]
        rand_idx = data[1]
        ll_node.random = linked_list_nodes[rand_idx] if rand_idx is not None else None
        ll_node.next = linked_list_nodes[i + 1] if i + 1 < n else None

    return linked_list_nodes[0]


def build_node_list(head: Optional[ListNode]) -> NodeList:
    if head is None:
        return []
    nodes: NodeList = []
    ll_nodes: List[ListNode] = []
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