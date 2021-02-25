# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3651/

# Score of Parentheses
# Given a balanced parentheses string S, compute the score of the string based
# on the following rule:

# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.

# Example 1:
# Input: "()"
# Output: 1

# Example 2:
# Input: "(())"
# Output: 2

# Example 3:
# Input: "()()"
# Output: 2
# Example 4:

# Input: "(()(()))"
# Output: 6

# Note:
# # S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50


from typing import Callable
from termcolor import colored


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        return self.scoreOfParentheses_stack(s)

    def scoreOfParentheses_stack(self, s: str) -> int:
        stack = []
        cur = 0
        for ch in s:
            if ch == "(":
                stack.append(cur)
                cur = 0
            else:
                cur += stack.pop() + max(cur, 1)
        return cur

    def scoreOfParentheses_count_core(self, s: str) -> int:
        res = 0
        depth = 0
        for a, b in zip(s, s[1:]):
            if a + b == "()":
                res += 2 ** depth
            if a == "(":
                depth += 1
            else:
                depth -= 1
        return res


SolutionFunc = Callable[[str], int]


def test_solution(s: str, expected: int) -> None:
    def test_impl(func: SolutionFunc, s: str, expected: int) -> None:
        r = func(s)
        if r == expected:
            print(colored(f"PASSED {func.__name__} => {s} score is {r}", "green"))
        else:
            print(
                colored(
                    f"PASSED {func.__name__} => {s} score is {r}, but expected: {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.scoreOfParentheses_stack, s, expected)
    test_impl(sln.scoreOfParentheses_count_core, s, expected)


if __name__ == "__main__":
    test_solution(s="(()(()))", expected=6)
