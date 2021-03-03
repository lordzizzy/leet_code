# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3658/

# Set Mismatch
# You have a set of integers s, which originally contains all the numbers from
# 1 to n. Unfortunately, due to some error, one of the numbers in s got
# duplicated to another number in the set, which results in repetition of one
# number and loss of another number.

# You are given an integer array nums representing the data status of this set
# after the error.

# Find the number that occurs twice and the number that is missing and return
# them in the form of an array.

# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]

# Example 2:
# Input: nums = [1,1]
# Output: [1,2]

# Constraints:
# 2 <= nums.length <= 10⁴
# 1 <= nums[i] <= 10⁴

from typing import Callable, List
from termcolor import colored


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return self.findErrorNums_sort(nums)

    def findErrorNums_sort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        t1 = (n * (n + 1)) // 2
        t = sum(nums)
        nums.sort()
        dup = 0
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                dup = nums[i]
        missing = t1 - t + dup
        return [dup, missing]

    def findErrorNums_set(self, nums: List[int]) -> List[int]:
        n = len(nums)
        b = sum(nums)
        c = sum(set(nums))
        a = (n * (n + 1)) // 2
        missing = a - c
        duplicate = b - c
        return [duplicate, missing]


SolutionFunc = Callable[[List[int]], List[int]]


def test_solution(nums: List[int], expected: List[int]) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], expected: List[int]) -> None:
        r = func(nums)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => duplicate, missing numbers in {nums} are {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => duplicate, missing numbers in {nums} are {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.findErrorNums_set, nums, expected)
    test_impl(sln.findErrorNums_sort, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[2, 2], expected=[2, 1])
    test_solution(nums=[1, 2, 2, 4], expected=[2, 3])
    test_solution(nums=[1, 1], expected=[1, 2])
