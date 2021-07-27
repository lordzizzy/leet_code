# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3828/s

#  3Sum Closest

# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Constraints:

# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4

from typing import Callable, List

from termcolor import colored


class Solution:
    # Time complexity: O(N^2)
    # Space complexity: O(1)
    def threeSumClosest_2ptrs(self, nums: List[int], target: int) -> int:
        N, diff = len(nums), 2 ** 32 - 1
        nums.sort()

        for i in range(N):
            lo, hi = i + 1, N - 1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break

        return target - diff


SolutionFunc = Callable[[List[int], int], int]


def test_solution(nums: List[int], target: int, expected: int) -> None:
    def test_impl(
        func: SolutionFunc, nums: List[int], target: int, expected: int
    ) -> None:
        res = func(nums, target)
        if res == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Closest sum to {target} with three integers in {nums} is {res}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Closest sum to {target} with three integers in {nums} is {res} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.threeSumClosest_2ptrs, nums, target, expected)


def main() -> None:
    test_solution(nums=[-1, 2, 1, -4], target=1, expected=2)


if __name__ == "__main__":
    main()
