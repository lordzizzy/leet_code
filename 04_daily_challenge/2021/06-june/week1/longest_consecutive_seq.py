# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3769/

# Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Constraints:
# 0 <= nums.length <= 10⁵
# -10⁹ <= nums[i] <= 10⁹

from typing import Callable, List, Set
from termcolor import colored


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return self.longestConsecutive_first_attempt(nums)

    def longestConsecutive_first_attempt(self, nums: List[int]) -> int:
        s = set(nums)
        visited: Set[int] = set()
        longest = 0
        for num in s:
            if num not in visited:
                cur = 1
                visited.add(num)

                fwd = num + 1
                while fwd in s:
                    cur += 1
                    fwd += 1
                    visited.add(fwd)

                bck = num - 1
                while bck in s:
                    cur += 1
                    bck -= 1
                    visited.add(bck)

                longest = max(longest, cur)
        return longest

    def longestConsecutive_fastest(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 in s:
                continue
            current = 1
            seq_num = num
            while seq_num + 1 in s:
                current += 1
                seq_num += 1
            longest = max(longest, current)
        return longest

    def longestConsecutive_best(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 not in s:
                next = num + 1
                while next in s:
                    next += 1
                longest = max(longest, next - num)
        return longest


SolutionFunc = Callable[[List[int]], int]


def test_solution(nums: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], expected: int) -> None:
        r = func(nums)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Longest consecutive sequence of numbers in {nums} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Longest consecutive sequence of numbers in {nums} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.longestConsecutive_first_attempt, nums, expected)
    test_impl(sln.longestConsecutive_fastest, nums, expected)
    test_impl(sln.longestConsecutive_best, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[100, 4, 200, 1, 3, 2], expected=4)
    test_solution(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1], expected=9)
