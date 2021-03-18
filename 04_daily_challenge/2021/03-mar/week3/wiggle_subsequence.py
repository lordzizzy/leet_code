# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3676/

# Wiggle Subsequence
# Given an integer array nums, return the length of the longest wiggle
# sequence.

# A wiggle sequence is a sequence where the differences between successive
# numbers strictly alternate between positive and negative. The first
# difference (if one exists) may be either positive or negative. A sequence
# with fewer than two elements is trivially a wiggle sequence.

# For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences
# (6, -3, 5, -7, 3) are alternately positive and negative.

# In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences,
# the first because its first two differences are positive and the second
# because its last difference is zero.

# A subsequence is obtained by deleting some elements (eventually, also zero)
# from the original sequence, leaving the remaining elements in their original
# order.

# Example 1:
# Input: nums = [1,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence.

# Example 2:
# Input: nums = [1,17,5,10,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that achieve this length. One is
# [1,17,10,13,10,16,8].

# Example 3:
# Input: nums = [1,2,3,4,5,6,7,8,9]
# Output: 2

# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000

# Follow up: Could you solve this in O(n) time?

from typing import Callable, List
from termcolor import colored


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        return self.wiggleMaxLength_greedy(nums)

    def wiggleMaxLength_greedy(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        prev_diff = nums[1] - nums[0]
        count = 2 if prev_diff != 0 else 1
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
                count += 1
                prev_diff = diff
        return count

    def wiggleMaxLength_greedy_alt(self, nums: List[int]) -> int:
        count = 1
        up = None
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and not up:
                count += 1
                up = True
            elif nums[i] < nums[i - 1] and up:
                count += 1
                up = False
        return count


SolutionFunc = Callable[[List[int]], int]


def test_solution(nums: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], expected: int) -> None:
        r = func(nums)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Longest wiggle subsequence in {nums} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Longest wiggle subsequence in {nums} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.wiggleMaxLength_greedy, nums, expected)
    test_impl(sln.wiggleMaxLength_greedy_alt, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[1, 7, 4, 9, 2, 5], expected=6)
    test_solution(nums=[1, 17, 5, 10, 13, 15, 10, 5, 16, 8], expected=7)
