# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/

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

from typing import List
from termcolor import colored
import math


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return self.findNumbers_log10_trick(nums)
        # return self.findNumbers_str_conv(nums)

    def findNumbers_str_conv(self, nums: List[int]) -> int:
        return sum(int(len(str(num)) % 2 == 0) for num in nums)

    def findNumbers_log10_trick(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            # So if number of digits is even, log10(n) will be odd.
            # Hence, we just need to do bitwise AND of log10(n) and 1 for odd check.
            res += int(math.log10(num)) & 1
        return res


def test_solution(nums: List[int], expected: int):
    def test_impl(func, nums: List[int], expected: int):
        r = func(nums)
        if r == expected:
            print(
                colored(f"PASSED {func.__name__} => {nums} have {r} numbers with even digits.", "green"))
        else:
            print(colored(
                f"FAILED {func.__name__} => {nums} have {r} numbers with even digits, but expected: {expected}", "red"))

    sln = Solution()
    test_impl(sln.findNumbers_str_conv, nums, expected)
    test_impl(sln.findNumbers_log10_trick, nums, expected)


def is_even_digit(num: int) -> bool:
    is_even = False
    while num:
        num >>= 1
        is_even = not is_even
    return is_even


if __name__ == "__main__":
    test_solution(nums=[12, 345, 2, 6, 7896], expected=2)
    test_solution(nums=[555, 901, 482, 1771], expected=1)
