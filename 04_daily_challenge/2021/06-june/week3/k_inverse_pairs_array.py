# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3784/

# K Inverse Pairs Array
# For an integer array nums, an inverse pair is a pair of integers [i, j] where
# 0 <= i < j < nums.length and nums[i] > nums[j].

# Given two integers n and k, return the number of different arrays consist of
# numbers from 1 to n such that there are exactly k inverse pairs. Since the
# answer can be huge, return it modulo 109 + 7.

# Example 1:
# Input: n = 3, k = 0
# Output: 1
# Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has
# exactly 0 inverse pairs.

# Example 2:
# Input: n = 3, k = 1
# Output: 2
# Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.

# Constraints:
# 1 <= n <= 1000
# 0 <= k <= 1000

from typing import Callable

from termcolor import colored


class Solution:
    # Time complexity: O(N^2 * K)
    def kInversePairs_dp_topdown(self, n: int, k: int) -> int:
        def dfs(n: int, k: int) -> int:
            if n == 0:
                return 0
            if k == 0:
                return 1
            inv = 0
            for i in range(min(k, n - 1) + 1):
                inv += dfs(n - 1, k - i) % int(10e9 + 7)
            return inv

        return dfs(n, k)


SolutionFunc = Callable[[int, int], int]


def test_solution(n: int, k: int, expected: int) -> None:
    def test_impl(func: SolutionFunc, n: int, k: int, expected: int) -> None:
        r = func(n, k)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Num of K inverse pairs in permutations of array of 1 to {n} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Num of K inverse pairs in permutations of array of 1 to {n} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.kInversePairs_dp_topdown, n, k, expected)


if __name__ == "__main__":
    test_solution(n=3, k=0, expected=1)
    test_solution(n=3, k=1, expected=2)
