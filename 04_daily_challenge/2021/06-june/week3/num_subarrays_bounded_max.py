# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3782/

# Number of Subarrays with Bounded Maximum
# We are given an array nums of positive integers, and two positive integers left and right (left <= right).

# Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least left and at most right.

# Example:
# Input:
# nums = [2, 1, 4, 3]
# left = 2
# right = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
# Note:
# left, right, and nums[i] will be an integer in the range [0, 10^9].
# The length of nums will be in the range of [1, 50000].

from typing import Callable, List
from termcolor import colored


class Solution:
    # Time complexity = O(N), Space complexity = O(1)
    def numSubarrayBoundedMax_sliding_window(
        self, nums: List[int], left: int, right: int
    ) -> int:
        l, r = -1, -1
        res = 0

        for i, num in enumerate(nums):
            if num >= left:
                l = i
            if num > right:
                r = i
            res += l - r

        return res

    # reference
    # https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/117723/Python-standard-DP-solution-with-explanation
    # let dp = number of subarrays so far at i
    # Time complexity = O(N), Space complexity = O(1)
    def numSubarrayBoundedMax_dp_bottom_up(
        self, nums: List[int], left: int, right: int
    ) -> int:
        res, dp, prev = 0, 0, -1

        for i, num in enumerate(nums):
            if num > right:
                dp = 0
                prev = i
            elif num >= left:
                dp = i - prev
            res += dp

        return res


SolutionFunc = Callable[[List[int], int, int], int]


def test_solution(nums: List[int], left: int, right: int, expected: int) -> None:
    def test_impl(
        func: SolutionFunc, nums: List[int], left: int, right: int, expected: int
    ) -> None:
        r = func(nums, left, right)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Number of contiguous, non-empty subarrays in {nums} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Number of contiguous, non-empty subarrays in {nums} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.numSubarrayBoundedMax_sliding_window, nums, left, right, expected)
    test_impl(sln.numSubarrayBoundedMax_dp_bottom_up, nums, left, right, expected)


if __name__ == "__main__":
    test_solution(nums=[2, 1, 4, 3], left=2, right=3, expected=3)
    test_solution(nums=[2, 9, 2, 5, 6], left=2, right=8, expected=7)
