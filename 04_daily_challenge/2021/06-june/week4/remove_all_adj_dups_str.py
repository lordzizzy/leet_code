# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3794/

# Remove All Adjacent Duplicates In String
# You are given a string s consisting of lowercase English letters. A duplicate
# removal consists of choosing two adjacent and equal letters and removing
# them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It
# can be proven that the answer is unique.


# Example 1:
# Input: s = "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent
# and equal, and this is the only possible move.  The result of this move is
# that the string is "aaca", of which only "aa" is possible, so the final
# string is "ca".

# Example 2:
# Input: s = "azxxzy"
# Output: "ay"


# Constraints:
# 1 <= s.length <= 10⁵
# s consists of lowercase English letters.

from typing import Callable
from termcolor import colored


class Solution:
    def removeDuplicates_bruteforce_dfs(self, s: str) -> str:
        def dfs(s: str) -> str:
            i = 0
            while i < len(s) - 1:
                if s[i] == s[i + 1]:
                    l = s[:i]
                    r = s[i + 2 :]
                    ns = l + r
                    return dfs(ns)
                i += 1
            return s

        return dfs(s)


SolutionFunc = Callable[[str], str]


def test_solution(s: str, expected: str) -> None:
    def test_impl(func: SolutionFunc, s: str, expected: str) -> None:
        r = func(s)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Remove all adjacent duplicates in string for {s} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Remove all adjacent duplicates in string for {s} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.removeDuplicates_bruteforce_dfs, s, expected)


if __name__ == "__main__":
    test_solution(s="abbaca", expected="ca")
    test_solution(s="azxxzy", expected="ay")
