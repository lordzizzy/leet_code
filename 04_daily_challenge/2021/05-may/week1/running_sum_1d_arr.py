# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3730/

# Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] =
# sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1,
# 1+1+1+1+1].

# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

# Constraints:
# 1 <= nums.length <= 1000
# -10⁶ <= nums[i] <= 10⁶

from typing import Callable, List
from termcolor import colored


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return self.runningSum_simple(nums)

    def runningSum_simple(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [nums[0]] * N
        for i in range(1, N):
            res[i] = res[i - 1] + nums[i]
        return res

    def runningSum_in_place(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


SolutionFunc = Callable[[List[int]], List[int]]


def test_solution(nums: List[int], expected: List[int]) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], expected: List[int]) -> None:
        r = func(nums)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Running sum of {nums} is {r}", "green"
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Running sum of {nums} is {r} but expected is {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.runningSum_simple, nums, expected)
    test_impl(sln.runningSum_in_place, nums.copy(), expected)


if __name__ == "__main__":
    test_solution(nums=[1, 2, 3, 4], expected=[1, 3, 6, 10])
    test_solution(nums=[1, 1, 1, 1, 1], expected=[1, 2, 3, 4, 5])
    test_solution(nums=[3, 1, 2, 10, 1], expected=[3, 4, 6, 16, 17])
