# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3713/

# Combination Sum IV
# Given an array of distinct integers nums and a target integer target, return
# the number of possible combinations that add up to target.

# The answer is guaranteed to fit in a 32-bit integer.

# Example 1:

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.

# Example 2:
# Input: nums = [9], target = 3
# Output: 0

# Constraints:
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000

# Follow up: What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?

# https://leetcode.com/problems/combination-sum-iv/discuss/85036/1ms-Java-DP-Solution-with-Detailed-Explanation

from typing import Callable, List
from termcolor import colored


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.combinationSum4_dp_topdown(nums, target)

    def combinationSum4_recursion(self, nums: List[int], target: int) -> int:
        def combs(nums: List[int], target: int) -> int:
            if target == 0:
                return 1
            res = 0
            for i in range(len(nums)):
                if target >= nums[i]:
                    res += combs(nums, target - nums[i])
            return res

        ans = combs(nums, target)
        return ans

    def combinationSum4_dp_topdown(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1)
        dp[0] = 1

        def combs(nums: List[int], target: int) -> int:
            if dp[target] != -1:
                return dp[target]
            res = 0
            for i in range(len(nums)):
                if target >= nums[i]:
                    res += combs(nums, target - nums[i])
            dp[target] = res
            return res

        return combs(nums, target)

    def combinationSum4_dp_bottom_up(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(target + 1):
            for n in nums:
                prevT = t - n
                if prevT < 0:
                    continue
                dp[t] += dp[prevT]
        return dp[target]


SolutionFunc = Callable[[List[int], int], int]


def test_solution(nums: List[int], target: int, expected: int) -> None:
    def test_impl(
        func: SolutionFunc, nums: List[int], target: int, expected: int
    ) -> None:
        r = func(nums, target)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Num Possible Combinations for any {nums} to add to {target} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Num Possible Combinations for any {nums} to add to {target} is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.combinationSum4_dp_topdown, nums, target, expected)
    test_impl(sln.combinationSum4_dp_bottom_up, nums, target, expected)


if __name__ == "__main__":
    test_solution(nums=[1, 2, 3], target=4, expected=7)
