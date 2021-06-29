# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/607/week-5-june-29th-june-30th/3796/

# Max Consecutive Ones III
# Given a binary array nums and an integer k, return the maximum number of
# consecutive 1's in the array if you can flip at most k 0's.

# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


# Constraints:
# 1 <= nums.length <= 10⁵
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

from typing import Callable, List

from termcolor import colored


class Solution:
    # reference
    # https://leetcode.com/problems/max-consecutive-ones-iii/discuss/719833/Python3-sliding-window-with-clear-example-explains-why-the-soln-works
    #
    # Time complexity: O(N)
    # Space complexity: O(1)
    def longestOnes_sliding_window(self, nums: List[int], k: int) -> int:
        l, r = 0, 0

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1

            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1

        return r - l + 1


SolutionFunc = Callable[[List[int], int], int]


def test_solution(nums: List[int], k: int, expected: int) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], k: int, expected: int) -> None:
        r = func(nums, k)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Maximum consecutive 1s for {nums} if you can flip at most {k} 0s is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Maximum consecutive 1s for {nums} if you can flip at most {k} 0s is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.longestOnes_sliding_window, nums, k, expected)


if __name__ == "__main__":
    test_solution(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2, expected=6)
    test_solution(
        nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3, expected=10
    )
