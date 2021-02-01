
# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3606/

# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:

# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


def checkSolution(nums: List[int], k: int, expected: int):
    s = Solution()
    largest = s.findKthLargest(nums, k)
    assert expected == largest, f"largest: {largest}, but expected: {expected}"


if __name__ == "__main__":
    checkSolution(nums=[3, 2, 1, 5, 6, 4], k=2, expected=5)
    checkSolution(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4, expected=4)
