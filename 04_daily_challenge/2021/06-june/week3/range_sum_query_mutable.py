# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3783/

# Range Sum Query - Mutable
# Given an integer array nums, handle multiple queries of the following types:

# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right
# inclusive where left <= right.

# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be val.
# int sumRange(int left, int right) Returns the sum of the elements of nums
# between indices left and right inclusive (i.e. nums[left] + nums[left + 1] +
# ... + nums[right]).


# Example 1:
# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]

# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1, 2, 5]
# numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8


# Constraints:

# 1 <= nums.length <= 3 * 10⁴
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# At most 3 * 10⁴ calls will be made to update and sumRange.


from itertools import accumulate
from typing import List, Optional, Protocol

from termcolor import colored


class NumArray(Protocol):
    def __init__(self, nums: List[int]):
        ...

    def update(self, index: int, val: int) -> None:
        ...

    def sumRange(self, left: int, right: int) -> int:
        ...


# TLE because update is too slow, O(N)
class NumArray_dp_caching(NumArray):
    def __init__(self, nums: List[int]):
        self._nums = nums
        self._dp = [0] + list(accumulate(nums))

    def update(self, index: int, val: int) -> None:
        diff = val - self._nums[index]
        self._nums[index] = val
        for i in range(index + 1, len(self._dp)):
            self._dp[i] += diff

    def sumRange(self, left: int, right: int) -> int:
        return self._dp[right + 1] - self._dp[left]


class Node:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.total = 0
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


# __init__  Time complexity: O(N)
# update    Time complexity: O(Log N)
# sumRange  Time complexity: O(Log N)
class NumArray_segment_tree(NumArray):
    def __init__(self, nums: List[int]):
        def create_tree(nums: List[int], l: int, r: int) -> Optional[Node]:
            # base case
            if l > r:
                return None

            # leaf node
            if l == r:
                node = Node(l, r)
                node.total = nums[l]
                return node

            mid = (l + r) // 2
            root = Node(l, r)

            # recursively build the segment tree
            root.left = create_tree(nums, l, mid)
            root.right = create_tree(nums, mid + 1, r)

            # total stores the sum of all leaves under root
            root.total = root.left.total + root.right.total

            return root

        self.root = create_tree(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        def update_val(root: Node, i: int, val: int) -> int:
            # base case
            if root.start == root.end:
                root.total = val
                return val

            mid = (root.start + root.end) // 2

            # if index less than mid, left must be in left subtree
            if i <= mid:
                update_val(root.left, i, val)
            else:
                update_val(root.right, i, val)

            root.total = root.left.total + root.right.total
            return root.total

        update_val(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def range_sum(root: Node, left: int, right: int):

            # If the range exactly matches the root, we already have the sum
            if root.start == left and root.end == right:
                return root.total

            mid = (root.start + root.end) // 2

            # If end of the range is less than the mid, the entire interval lies
            # in the left subtree
            if right <= mid:
                return range_sum(root.left, left, right)

            # If start of the interval is greater than mid, the entire inteval lies
            # in the right subtree
            elif left >= mid + 1:
                return range_sum(root.right, left, right)

            # Otherwise, the interval is split. So we calculate the sum recursively,
            # by splitting the interval
            else:
                return range_sum(root.left, left, mid) + range_sum(root.right, mid + 1, right)

        return range_sum(self.root, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


def test_solution(numArray: NumArray) -> None:
    r1 = numArray.sumRange(0, 2)
    numArray.update(1, 2)
    r2 = numArray.sumRange(0, 2)

    if r1 == 9 and r2 == 8:
        print(colored(f"PASSED {type(numArray).__name__}", "green"))
    else:
        print(colored(f"FAILED {type(numArray).__name__}", "red"))


if __name__ == "__main__":
    test_solution(NumArray_dp_caching(nums=[1, 3, 5]))
    test_solution(NumArray_segment_tree(nums=[1, 3, 5]))
