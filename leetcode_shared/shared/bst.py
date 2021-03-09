from __future__ import annotations
from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    val: int
    left: Optional[TreeNode]
    right: Optional[TreeNode]

    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"<{self.val} {self.left}, {self.right}>"


def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    it = iter(nodes)
    val = next(it)
    if val is None:
        raise AssertionError(f"First node's value cannot be None")
    tree = TreeNode(val)
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


def build_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []
    res = []
    fringe = deque([root])
    res.append(root.val)
    while len(fringe) > 0:
        head = fringe.popleft()
        if head.left:
            res.append(head.left.val)
            fringe.append(head.left)
        else:
            res.append(None)
        if head.right:
            res.append(head.right.val)
            fringe.append(head.right)
        else:
            res.append(None)
    return res
