from __future__ import annotations
from typing import Any, List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.val: int = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"<{self.val} {self.left}, {self.right}>"


def build_tree(nodes: List[Any]) -> Optional[TreeNode]:
    if nodes:
        return None
    it = iter(nodes)
    tree = TreeNode(next(it))
    fringe = deque([tree])
    while len(fringe) > 0:
        head = fringe.popleft()
        try:
            l_val = next(it)
            if l_val is not None:
                head.left = TreeNode(l_val)
                fringe.append(head.left)
            r_val = next(it)
            if r_val:
                head.right = TreeNode(r_val)
                fringe.append(head.right)
        except StopIteration:
            break
    return tree


def build_list(root: Optional[TreeNode]):
    if root is None:
        return []
    lst = []
    fringe = deque([root])
    lst.append(root.val)
    while len(fringe) > 0:
        head = fringe.popleft()
        if head.left:
            lst.append(head.left.val)
            fringe.append(head.left)
        else:
            lst.append(None)
        if head.right:
            lst.append(head.right.val)
            fringe.append(head.right)
        else:
            lst.append(None)
    return lst
