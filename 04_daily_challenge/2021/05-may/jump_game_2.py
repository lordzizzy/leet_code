# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3732/

# Jump Game II
# Given an array of non-negative integers nums, you are initially positioned at
# the first index of the array.

# Each element in the array represents your maximum jump length at that
# position.

# Your goal is to reach the last index in the minimum number of jumps.

# You can assume that you can always reach the last index.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2

# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 10⁵

from typing import Callable, List
from termcolor import colored


class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.jump_greedy(nums)

    def jump_greedy(self, nums: List[int]) -> int:
        cnt, end, best = 0, 0, 0
        for i in range(len(nums) - 1):
            best = max(best, i + nums[i])
            if i == end:
                cnt += 1
                end = best
        return cnt

    def jump_2ptrs(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        l, r = 0, nums[0]
        cnt = 1
        while r < len(nums) - 1:
            cnt += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return cnt


SolutionFunc = Callable[[List[int]], int]


def test_solution(nums: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], expected: int) -> None:
        r = func(nums)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Min num of jumps for {nums} from start to end is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"PASSED {func.__name__} => Min num of jumps for {nums} from start to end is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.jump_greedy, nums, expected)
    test_impl(sln.jump_2ptrs, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[2, 3, 1, 1, 4], expected=2)
    test_solution(nums=[2, 3, 0, 1, 4], expected=2)
