# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3812/

# Find Peak Element
# A peak element is an element that is strictly greater than its neighbors.

# Given an integer array nums, find a peak element, and return its index. If
# the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞.

# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2, or index number 5 where the peak element is 6.

# Constraints:

# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.

from typing import Callable, List

from termcolor import colored


class Solution:
    # Time complexity: O(N)
    # Space complexity: O(1)
    def findPeakElement_linearscan(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1

    # Time complexity: O(log N)
    # Space complexity: O(log N)
    def findPeakElement_binarysearch_recursive(self, nums: List[int]) -> int:
        def binary_search(left: int, right: int) -> int:
            if left == right:
                return left
            mid = (left + right) // 2
            # if mid is descending, we search to the left, else to the right
            if nums[mid] > nums[mid + 1]:
                return binary_search(left, mid)
            else:
                return binary_search(mid + 1, right)

        return binary_search(0, len(nums) - 1)

    # Time complexity: O(log N)
    # Space complexity: O(1)
    def findPeakElement_binarysearch_iterative(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # if mid is descending, we search to the left, else to the right
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left


SolutionFunc = Callable[[List[int]], int]


def test_solution(nums: List[int], expected: List[int]) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], expected: List[int]) -> None:
        r = func(nums)
        if r in expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Found a index of peak elem in {nums} is {r}, with peak indexes {expected}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Found a index of peak elem in {nums} is {r} expected any in peak indexes {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.findPeakElement_linearscan, nums, expected)
    test_impl(sln.findPeakElement_binarysearch_recursive, nums, expected)
    test_impl(sln.findPeakElement_binarysearch_iterative, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[1, 2, 3, 1], expected=[2])
    test_solution(nums=[1, 2, 1, 3, 5, 6, 4], expected=[1, 5])
