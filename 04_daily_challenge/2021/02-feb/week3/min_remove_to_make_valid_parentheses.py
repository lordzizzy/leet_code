# Minimum Remove to Make Valid Parentheses
# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any
# positions ) so that the resulting parentheses string is valid and return any
# valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.


# Example 1:
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

# Example 2:
# Input: s = "a)b(c)d"
# Output: "ab(c)d"

# Example 3:
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.

# Example 4:
# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"

# Constraints:
# 1 <= s.length <= 10⁵
# s[i] is one of  '(' , ')' and lowercase English letters.

# TODO:
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/419402/JavaC%2B%2B-Stack

from typing import Callable
from termcolor import colored


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        return self.minRemoveToMakeValid_stack(s)

    def minRemoveToMakeValid_stack(self, s: str) -> str:
        ss = list(s)
        stack = []
        for i, ch in enumerate(ss):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    ss[i] = ""

        while stack:
            ss[stack.pop()] = ""

        return "".join(ss)


SolutionFunc = Callable[[str], str]


def test_solution(s: str, expected: str) -> None:
    def test_impl(func: SolutionFunc, s: str, expected: str) -> None:
        r = func(s)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {s} with valid parentheses is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {s} with valid parentheses is {r}, but expected: {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.minRemoveToMakeValid, s, expected)


if __name__ == "__main__":
    test_solution(s="lee(t(c)o)de)", expected="lee(t(c)o)de")
    test_solution(s="a)b(c)d", expected="ab(c)d")
    test_solution(s="))((", expected="")
    test_solution(s="(a(b(c)d)", expected="a(b(c)d)")
    test_solution(s="())()(((", expected="()()")
