# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3807/

# Maximum Length of Repeated Subarray (AKA - longest common substring)

# Given two integer arrays nums1 and nums2, return the maximum length of a
# subarray that appears in both arrays.

# Example 1:
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].

# Example 2:
# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100

# Same solution or approach to solve longest common substring LCS

from typing import Callable, List

from termcolor import colored


class Solution:
    def findLength_bruteforce(self, nums1: List[int], nums2: List[int]) -> int:
        raise NotImplementedError()

    def findLength_dp_bottomup(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
        return ans

    def findLength_binarysearch(self, nums1: List[int], nums2: List[int]) -> int:
        raise NotImplementedError()


SolutionFunc = Callable[[List[int], List[int]], int]


def test_solution(nums1: List[int], nums2: List[int], expected: int) -> None:
    def test_impl(
        func: SolutionFunc, nums1: List[int], nums2: List[int], expected: int
    ) -> None:
        r = func(nums1, nums2)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Max length of subarray of {nums1} and {nums2} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Max length of subarray of {nums1} and {nums2} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.findLength_dp_bottomup, nums1, nums2, expected)


if __name__ == "__main__":
    test_solution(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7], expected=3)
    test_solution(nums1=[0, 0, 0, 0, 0], nums2=[0, 0, 0, 0, 0], expected=5)
