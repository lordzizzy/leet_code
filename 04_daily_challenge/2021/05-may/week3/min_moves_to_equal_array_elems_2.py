# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3748/

# Minimum Moves to Equal Array Elements II

# Given an integer array nums of size n, return the minimum number of moves
# required to make all array elements equal.

# In one move, you can increment or decrement an element of the array by 1.

# Example 1:
# Input: nums = [1,2,3]
# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

# Example 2:
# Input: nums = [1,10,2,9]
# Output: 16

# Constraints:
# n == nums.length
# 1 <= nums.length <= 10⁵
# -10⁹ <= nums[i] <= 10⁹

from typing import Callable, List
from termcolor import colored


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = sorted(nums)[len(nums) // 2]
        return sum(abs(n - median) for n in nums)


SolutionFunc = Callable[[List[int]], int]


def test_solution(nums: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], expected: int) -> None:
        r = func(nums)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Min moves to equal array elems {nums} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Min moves to equal array elems {nums} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.minMoves2, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[1, 2, 3], expected=2)
    test_solution(nums=[1, 10, 2, 9], expected=16)
