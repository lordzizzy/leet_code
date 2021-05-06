# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/597/week-5-april-29th-april-30th/3725/

# Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# Follow up: Could you write an algorithm with O(log n) runtime complexity?


# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

# Constraints:
# 0 <= nums.length <= 10⁵
# -10⁹ <= nums[i] <= 10⁹
# nums is a non-decreasing array.
# -10⁹ <= target <= 10⁹

from typing import Callable, List
from termcolor import colored

import bisect


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.searchRange_logn_divide_and_conquer(nums, target)

    def searchRange_logn_divide_and_conquer(
        self, nums: List[int], target: int
    ) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        def search(lo: int, hi: int) -> List[int]:
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mid = (lo + hi) // 2
                l, r = search(lo, mid), search(mid + 1, hi)
                return max(l, r) if -1 in l + r else [l[0], r[1]]
            return [-1, -1]

        return search(0, len(nums) - 1)

    def searchRange_2_binary_searches(self, nums: List[int], target: int) -> List[int]:
        def bin_search(n: int) -> int:
            lo = 0
            hi = len(nums)
            while lo < hi:
                mid: int = (lo + hi) // 2
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        lo = bin_search(target)
        return (
            [lo, bin_search(target + 1) - 1]
            if target in nums[lo : lo + 1]
            else [-1, -1]
        )

    def searchRange_2_binary_searches_pythonic(
        self, nums: List[int], target: int
    ) -> List[int]:
        lo = bisect.bisect_left(nums, target)
        return (
            [lo, bisect.bisect(nums, target) - 1]
            if target in nums[lo : lo + 1]
            else [-1, -1]
        )


SolutionFunc = Callable[[List[int], int], List[int]]


def test_solution(nums: List[int], target: int, expected: List[int]) -> None:
    def test_impl(
        func: SolutionFunc, nums: List[int], target: int, expected: List[int]
    ) -> None:
        r = func(nums, target)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Start and end pos of {target} in {nums} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Start and end pos of {target} in {nums} is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.searchRange_2_binary_searches, nums, target, expected)
    test_impl(sln.searchRange_2_binary_searches_pythonic, nums, target, expected)


if __name__ == "__main__":
    test_solution(nums=[], target=1, expected=[-1, -1])
    test_solution(nums=[5, 7, 7, 8, 8, 10], target=8, expected=[3, 4])
