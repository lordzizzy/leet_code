# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3731/

# Non-decreasing Array
# Given an array nums with n integers, your task is to check if it could become
# non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for
# every i (0-based) such that (0 <= i <= n - 2).

# Example 1:
# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

# Example 2:
# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most one
# element.

# Constraints:
# n == nums.length
# 1 <= n <= 10⁴
# -10⁵ <= nums[i] <= 10⁵


from typing import Callable, List
from termcolor import colored


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        return self.checkPossibility_simple(nums)

    def checkPossibility_simple(self, nums: List[int]) -> bool:
        # An array of 2 numbers can always be fixed up
        if len(nums) <= 2:
            return True

        count = 0
        idx = -1
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                if count:
                    # Only one outlier allowed
                    return False
                else:
                    count += 1
                    idx = i

        if not count:
            return True

        # If idx == 0, nums[0] can be dropped to fix the sequence
        # If idx == len(nums)-2, nums[len(nums)-1] can be dropped to fix the sequence
        if idx == 0 or idx == len(nums) - 2:
            return True

        # Check if nums[idx] can be dropped to fix the sequence
        if nums[idx + 1] >= nums[idx - 1]:
            return True
        # Check if nums[idx+1] can be dropped to fix the sequence
        if nums[idx + 2] >= nums[idx]:
            return True

        # No way to fix the sequence
        return False

    # Fastest sample 156ms
    def checkPossibility_elegant(self, nums: List[int]) -> bool:
        res = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                res += 1
                if (
                    i > 0
                    and i < len(nums) - 2
                    and nums[i - 1] > nums[i + 1]
                    and nums[i] > nums[i + 2]
                ):
                    return False
        return res < 2


SolutionFunc = Callable[[List[int]], bool]


def test_solution(nums: List[int], expected: bool) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], expected: bool) -> None:
        r = func(nums)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Possibility of modifying {nums} to be non-decreasing is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} Possibility of modifying {nums} to be non-decreasing is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.checkPossibility_simple, nums, expected)
    test_impl(sln.checkPossibility_elegant, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[4, 2, 3], expected=True)
    test_solution(nums=[4, 2, 1], expected=False)
    test_solution(nums=[1, 3, 2], expected=True)
    test_solution(nums=[5, 7, 1, 8], expected=True)
    test_solution(nums=[3, 4, 2, 3], expected=False)
