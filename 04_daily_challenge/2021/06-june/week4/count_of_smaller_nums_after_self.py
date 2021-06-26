# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3792/

# Count of Smaller Numbers After Self
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].

# Example 1:
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.

# Example 2:
# Input: nums = [-1]
# Output: [0]

# Example 3:
# Input: nums = [-1,-1]
# Output: [0,0]

# Constraints:

# 1 <= nums.length <= 10⁵
# -10⁴ <= nums[i] <= 10⁴

from typing import Callable, List

from termcolor import colored


class Solution:
    def countSmaller_brute_force(self, nums: List[int]) -> List[int]:
        N = len(nums)
        counts = [0] * N
        for i in range(N - 1):
            for j in range(i + 1, N):
                if nums[i] > nums[j]:
                    counts[i] += 1
        return counts


SolutionFunc = Callable[[List[int]], List[int]]


def test_solution(nums: List[int], expected: List[int]) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], expected: List[int]) -> None:
        r = func(nums)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Counts of smaller numbers after self for {nums} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Counts of smaller numbers after self for {nums} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.countSmaller_brute_force, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[5, 2, 6, 1], expected=[2, 1, 1, 0])
    test_solution(nums=[-1], expected=[0])
    test_solution(nums=[-1, -1], expected=[0, 0])
