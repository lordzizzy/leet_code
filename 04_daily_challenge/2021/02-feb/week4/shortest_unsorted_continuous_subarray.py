# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3652/

# Shortest Unsorted Continuous Subarray
# Given an integer array nums, you need to find one continuous subarray that if
# you only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order.

# Return the shortest such subarray and output its length.

# Example 1:
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 0

# Example 3:
# Input: nums = [1]
# Output: 0

# Constraints:
# 1 <= nums.length <= 10⁴
# -10⁵ <= nums[i] <= 10⁵

# Follow up: Can you solve it in O(n) time complexity?

from typing import Callable, List
from termcolor import colored


class Solution:
    def findUnsorted(self, nums: List[int]) -> int:
        return self.findUnsortedSubarray_no_sort(nums)

    def findUnsortedSubarray_no_sort(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        l, r = 0, n - 1

        # find first non-ascending
        while l < n - 1 and nums[l] <= nums[l + 1]:
            l += 1

        # find first non-descending
        while r > 0 and nums[r] >= nums[r - 1]:
            r -= 1

        if l > r:
            return 0

        temp = nums[l : r + 1]
        temp_min = min(temp)
        temp_max = max(temp)

        while l > 0 and temp_min < nums[l - 1]:
            l -= 1

        while r < n - 1 and temp_max > nums[r + 1]:
            r += 1

        return r - l + 1

    def findUnsortedSubarray_sorted(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        if sorted_nums == nums:
            return 0
        l, r = 0, len(nums) - 1
        while nums[l] == sorted_nums[l]:
            l += 1
        while nums[r] == sorted_nums[r]:
            r -= 1
        return r - l + 1


SolutionFunc = Callable[[List[int]], int]


def test_solution(nums: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], expected: int) -> None:
        r = func(nums)
        if r == expected:
            print(
                colored(
                    f"PASSED => {func.__name__} => shortest unsorted continuous subarray in {nums} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED => {func.__name__} => shortest unsorted continuous subarray in {nums} is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.findUnsortedSubarray_no_sort, nums, expected)
    test_impl(sln.findUnsortedSubarray_sorted, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[2, 1], expected=2)
    test_solution(nums=[2, 3, 3, 2, 4], expected=3)
    test_solution(nums=[1, 3, 2, 3, 3], expected=2)
    test_solution(nums=[1, 2, 3, 3, 3], expected=0)
    test_solution(nums=[1, 3, 2, 2, 2], expected=4)
    test_solution(nums=[2, 6, 4, 8, 10, 9, 15], expected=5)
    test_solution(nums=[1, 2, 3, 4], expected=0)
    test_solution(nums=[1], expected=0)
    test_solution(nums=[], expected=0)
