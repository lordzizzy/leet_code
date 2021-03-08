# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3609/

# Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Example 3:
# Input: s = "a"
# Output: "a"

# Example 4:
# Input: s = "ac"
# Output: "a"

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case)


from typing import Callable
from termcolor import colored


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.longestPalindrome_expand_from_center(s)

    def longestPalindrome_expand_from_center(self, s: str) -> str:
        def expand(s: str, left: int, right: int) -> str:
            n = len(s)
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        res = ""
        for i in range(0, len(s)):
            # for the odd case of "aba"
            s1 = expand(s, i, i)
            # for the even case of "abba"
            s2 = expand(s, i, i + 1)

            # select whichever is the biggest
            s1 = s1 if len(s1) > len(s2) else s2
            res = res if len(res) > len(s1) else s1

        return res


SolutionFunc = Callable[[str], str]


def test_solution(s: str, expected: str) -> None:
    def test_impl(func: SolutionFunc, s: str, expected: str) -> None:
        r = func(s)
        if len(r) == len(expected):
            print(
                colored(
                    f"PASSED {func.__name__} => Longest palindromic substring for {s} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Longest palindromic substring for {s} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.longestPalindrome_expand_from_center, s, expected)


if __name__ == "__main__":
    test_solution(s="babad", expected="bab")
    test_solution(s="cbbd", expected="bb")
    test_solution(s="a", expected="a")
    test_solution(s="ac", expected="a")
