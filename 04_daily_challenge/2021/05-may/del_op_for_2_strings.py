# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3734/

# Delete Operation for Two Strings
# Given two strings word1 and word2, return the minimum number of steps
# required to make word1 and word2 the same.

# In one step, you can delete exactly one character in either string.

# Example 1:
# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make
# "eat" to "ea".

# Example 2:
# Input: word1 = "leetcode", word2 = "etco"
# Output: 4

# Constraints:
# 1 <= word1.length, word2.length <= 500
# word1 and word2 consist of only lowercase English letters.

# https://leetcode.com/problems/delete-operation-for-two-strings/solution/


from typing import Callable
from termcolor import colored
from itertools import product


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.minDistance_2d_dp_LCS(word1, word2)

    def minDistance_2d_dp_LCS(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, j in product(range(m), range(n)):
            dp[i + 1][j + 1] = max(
                dp[i][j + 1], dp[i + 1][j], dp[i][j] + int(word1[i] == word2[j])
            )
        return m + n - (2 * dp[m][n])


SolutionFunc = Callable[[str, str], int]


def test_solution(word1: str, word2: str, expected: int) -> None:
    def test_impl(func: SolutionFunc, word1: str, word2: str, expected: int) -> None:
        r = func(word1, word2)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Min steps to make {word1} and {word2} the same is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Min steps to make {word1} and {word2} the same is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.minDistance_2d_dp_LCS, word1, word2, expected)


if __name__ == "__main__":
    test_solution(word1="sea", word2="eat", expected=2)
    test_solution(word1="leetcode", word2="etco", expected=4)
