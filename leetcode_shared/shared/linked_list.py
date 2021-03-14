from __future__ import annotations
from typing import Optional, List


class ListNode:
    def __init__(self, val: int, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        res = ""
        head = self
        while head:
            res += f"{head.val}->"
            if head.next is None:
                res += "None"
            head = head.next
        return res


NodeDataList = List[int]


def build_linked_list(nodes: NodeDataList) -> Optional[ListNode]:
    if not nodes:
        return None
    res: List[ListNode] = []
    # create linked list node and populate values
    for num in nodes:
        res.append(ListNode(val=num))
    # set next links foreach linked list node
    for i, node in enumerate(res):
        node.next = res[i + 1] if i + 1 < len(nodes) else None

    return res[0]


def build_node_data_list(head: Optional[ListNode]) -> NodeDataList:
    if head is None:
        return []
    res: NodeDataList = []
    while head:
        res.append(head.val)
        head = head.next
    return res