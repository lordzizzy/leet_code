# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3765/

# Interleaving String
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
# s1 and s2.

# An interleaving of two strings s and t is a configuration where they are
# divided into non-empty substrings such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 +
# t3 + s3 + ...

# Note: a + b is the concatenation of strings a and b.

# Example 1:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true

# Example 2:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false

# Example 3:
# Input: s1 = "", s2 = "", s3 = ""
# Output: true

# Constraints:
# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.

# Follow up: Could you solve it using only O(s2.length) additional memory
# space?

from typing import Callable
from termcolor import colored
from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.isInterleave_bruteforce_recurse_TLE(s1, s2, s3)

    def isInterleave_bruteforce_recurse_TLE(self, s1: str, s2: str, s3: str) -> bool:
        M, N = len(s1), len(s2)

        def is_interleaved(i: int, j: int, res: str) -> bool:
            if res == s3 and i == M and j == N:
                return True
            return (i < M and is_interleaved(i + 1, j, res + s1[i])) or (
                j < N and is_interleaved(i, j + 1, res + s2[j])
            )

        return M + N == len(s3) and is_interleaved(0, 0, "")

    def isInterleave_dp_top_down(self, s1: str, s2: str, s3: str) -> bool:
        M, N = len(s1), len(s2)

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> bool:
            if i == M and j == N:
                return True
            return (i < M and s1[i] == s3[i + j] and dp(i + 1, j)) or (
                j < N and s2[j] == s3[i + j] and dp(i, j + 1)
            )

        return M + N == len(s3) and dp(0, 0)

    def isInterleave_dp_bottom_up_2d(self, s1: str, s2: str, s3: str) -> bool:
        M, N = len(s1), len(s2)
        dp = [[False] * (N + 1) for _ in range(M + 1)]
        dp[M][N] = True
        for i in reversed(range(M + 1)):
            for j in reversed(range(N + 1)):
                if i < M and s1[i] == s3[i + j]:
                    dp[i][j] |= dp[i + 1][j]
                if j < N and s2[j] == s3[i + j]:
                    dp[i][j] |= dp[i][j + 1]
        return dp[0][0]

    def isInterleave_dp_bottom_up_1d(self, s1: str, s2: str, s3: str) -> bool:
        M, N = len(s1), len(s2)
        if M + N != len(s3):
            return False
        dp = [False] * (N + 1)
        for i in range(M + 1):
            for j in range(N + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (
                        dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                    )
        return dp[-1]


SolutionFunc = Callable[[str, str, str], bool]


def test_solution(s1: str, s2: str, s3: str, expected: bool) -> None:
    def test_impl(
        func: SolutionFunc, s1: str, s2: str, s3: str, expected: bool
    ) -> None:
        r = func(s1, s2, s3)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {s3} is interleaving of {s1} and {s2} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {s3} is interleaving of {s1} and {s2} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.isInterleave_bruteforce_recurse_TLE, s1, s2, s3, expected)
    test_impl(sln.isInterleave_dp_top_down, s1, s2, s3, expected)
    test_impl(sln.isInterleave_dp_bottom_up_2d, s1, s2, s3, expected)
    test_impl(sln.isInterleave_dp_bottom_up_1d, s1, s2, s3, expected)


if __name__ == "__main__":
    test_solution(s1="abc", s2="bcd", s3="abcbdc", expected=True)
    test_solution(s1="aabcc", s2="dbbca", s3="aadbbcbcac", expected=True)
    test_solution(s1="aabcc", s2="dbbca", s3="aadbbbaccc", expected=False)
