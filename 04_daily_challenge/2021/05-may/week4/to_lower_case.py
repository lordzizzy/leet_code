# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3754/

# To Lower Case
# Given a string s, return the string after replacing every uppercase letter
# with the same lowercase letter.

# Example 1:
# Input: s = "Hello"
# Output: "hello"

# Example 2:
# Input: s = "here"
# Output: "here"
# Example 3:

# Input: s = "LOVELY"
# Output: "lovely"

# Constraints:
# 1 <= s.length <= 100
# s consists of printable ASCII characters.

from typing import Callable
from termcolor import colored


class Solution:
    def toLowerCase(self, s: str) -> str:
        # use generators but supposedly slower
        # https://stackoverflow.com/questions/9060653/list-comprehension-without-in-python/9061024#9061024
        # return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in
        # s)
        # alternatively
        # return "".join([chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in s])
        return "".join([chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in s])


SolutionFunc = Callable[[str], str]


def test_solution(s: str, expected: str) -> None:
    def test_impl(func: SolutionFunc, s: str, expected: str) -> None:
        r = func(s)
        if r == expected:
            print(
                colored(f"PASSED {func.__name__} => {s} to lowercase is {r}", "green")
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {s} to lowercase is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.toLowerCase, s, expected)


if __name__ == "__main__":
    test_solution(s="Hello", expected="hello")
    test_solution(s="here", expected="here")
    test_solution(s="LOVELY", expected="lovely")
