# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3659/

#  Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return
# the only number in the range that is missing from the array.

# Follow up: Could you implement a solution using only O(1) extra space
# complexity and O(n) runtime complexity?

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range
# [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range
# [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range
# [0,9]. 8 is the missing number in the range since it does not appear in nums.

# Example 4:
# Input: nums = [0]
# Output: 1
# Explanation: n = 1 since there is 1 number, so all numbers are in the range
# [0,1]. 1 is the missing number in the range since it does not appear in nums.

# Constraints:
# n == nums.length
# 1 <= n <= 10⁴
# 0 <= nums[i] <= n
# All the numbers of nums are unique.

from typing import Callable, List
from termcolor import colored


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return self.missingNumber_sort_and_check(nums)

    def missingNumber_sort_and_check(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] != i:
                return i
        return n

    def missingNumber_formula(self, nums: List[int]) -> int:
        n = len(nums)
        return ((n * (n + 1)) // 2) - sum(nums)


SolutionFunc = Callable[[List[int]], int]


def test_solution(nums: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], expected: int) -> None:
        r = func(nums)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => missing num from {nums} is {r}", "green"
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => missing num from {nums} is {r} but expected is {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.missingNumber_sort_and_check, nums, expected)
    test_impl(sln.missingNumber_formula, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[3, 0, 1], expected=2)
    test_solution(nums=[0, 1], expected=2)
    test_solution(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1], expected=8)
