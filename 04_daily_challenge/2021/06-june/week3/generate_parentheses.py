# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3781/

# Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]

# Constraints:
# 1 <= n <= 8

from typing import Callable, List, Optional
from termcolor import colored
from functools import lru_cache


class Solution:
    def generateParenthesis_dp(self, n: int) -> List[str]:
        dp: List[List[str]] = [[] for _ in range(n + 1)]
        dp[0].append("")

        for i in range(n + 1):
            for j in range(i):
                dp[i] += ["(" + x + ")" + y for x in dp[j] for y in dp[i - 1 - j]]

        return dp[n]

    def generateParenthesis_dp_2(self, n: int) -> List[str]:
        @lru_cache(maxsize=None)
        def generate(n: int) -> List[str]:
            if n == 0:
                return [""]
            if n == 1:
                return ["()"]

            result: List[str] = []
            for x in range(n):
                for l in generate(x):
                    for r in generate(n - 1 - x):
                        print(f"x:{x}, l:{l}, r:{r}")
                        result.append("(" + l + ")" + r)
            return result

        return generate(n)


SolutionFunc = Callable[[int], List[str]]


def test_solution(n: int, expected: List[str]) -> None:
    def test_impl(func: SolutionFunc, n: int, expected: List[str]) -> None:
        r = func(n)
        if sorted(r) == sorted(expected):
            print(
                colored(
                    f"PASSED {func.__name__} => All combinations of well formed parentheses for {n} pairs of parentheses is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => All combinations of well formed parentheses for {n} pairs of parentheses is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    # test_impl(sln.generateParenthesis_dp, n, expected)
    test_impl(sln.generateParenthesis_dp_2, n, expected)


if __name__ == "__main__":
    test_solution(n=3, expected=["((()))", "(()())", "(())()", "()(())", "()()()"])
    test_solution(n=1, expected=["()"])
