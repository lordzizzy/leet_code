# https://leetcode.com/problems/longest-increasing-subsequence/

# 300. Longest Increasing Subsequence

# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.

# A subsequence is a sequence that can be derived from an array by deleting
# some or no elements without changing the order of the remaining elements. For
# example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

# Constraints:

# 1 <= nums.length <= 2500
# -10⁴ <= nums[i] <= 10⁴

# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
# complexity?

from bisect import bisect_left
from typing import Callable, List

from termcolor import colored

# references
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308


class Solution:
    # let dp[i] = len of longest increasing subsequence at i
    # Time complexity: O(N^2)
    # Space complexity: O(N)
    def lengthOfLIS_dp_bottomup(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N

        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    # https://leetcode.com/problems/longest-increasing-subsequence/discuss/667975/Python-3-Lines-dp-with-binary-search-explained
    # let dp[i] = min value so far at i
    # Time complexity: O(N logN)
    # Space complexity O(N)
    def lengthOfLIS_dp_binarysearch(self, nums: List[int]) -> int:
        dp: List[int] = []

        for elem in nums:
            idx = bisect_left(dp, elem)
            if idx == len(dp):
                dp.append(elem)
            else:
                dp[idx] = elem

        return len(dp)


SolutionFunc = Callable[[List[int]], int]


def test_solution(nums: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, nums: List[int], expected: int) -> None:
        r = func(nums)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Longest increasing subsequence length of {nums} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Longest increasing subsequence length of {nums} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.lengthOfLIS_dp_bottomup, nums, expected)
    test_impl(sln.lengthOfLIS_dp_binarysearch, nums, expected)


if __name__ == "__main__":
    test_solution(nums=[10, 9, 2, 5, 3, 7, 101, 18], expected=4)
    test_solution(nums=[0, 1, 0, 3, 2, 3], expected=4)
    test_solution(nums=[7, 7, 7, 7, 7, 7, 7], expected=1)
