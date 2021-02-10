# Find Numbers with Even Number of Digits
# Given an array nums of integers, return how many of them contain an even number of digits.

# Example 1:
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.

# Example 2:
# Input: nums = [555,901,482,1771]
# Output: 1
# Explanation:
# Only 1771 contains an even number of digits.

# Constraints:
# 1 <= nums.length <= 500
# 1 <= nums[i] <= 10^5

from typing import Callable, List
from termcolor import colored

from math import log10


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return self.findNumbers_log10(nums)

    def findNumbers_log10(self, nums: List[int]) -> int:
        return sum([int(log10(num)) & 1 for num in nums])

    def findNumbers_str_conv(self, nums: List[int]) -> int:
        return sum([len(str(num)) % 2 == 0 for num in nums])


def test_solution(nums: List[int], expected: int):
    SolutionFunc = Callable[[List[int]], int]

    def test_impl(func: SolutionFunc, nums: List[int], expected: int):
        r = func(nums)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {nums} has {r} numbers with even digits.",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {nums} has {r} numbers with even digits, but expected: {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.findNumbers_log10, nums, expected)
    test_impl(sln.findNumbers_str_conv, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[12, 345, 2, 6, 7896], expected=2)
    test_solution(nums=[555, 901, 482, 1771], expected=1)
