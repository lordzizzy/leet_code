# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3636/

# Valid Anagram
# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

from typing import Callable, Counter, DefaultDict
from termcolor import colored


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.isAnagram_counter(s, t)

    def isAnagram_sort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram_dict(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lookup = DefaultDict[str, int](lambda: 0)
        for char in s:
            lookup[char] += 1
        for char in t:
            lookup[char] -= 1
            if lookup[char] < 0:
                return False
        return True

    def isAnagram_counter(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


SolutionFunc = Callable[[str, str], bool]


def test_solution(s: str, t: str, expected: bool):
    def test_imp(func: SolutionFunc, s: str, t: str, expected: bool):
        r = func(s, t)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {t} is an anagram of {s} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"PASSED {func.__name__} => {t} is an anagram of {s} is {r}, but expected: {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_imp(sln.isAnagram_counter, s, t, expected)
    test_imp(sln.isAnagram_dict, s, t, expected)
    test_imp(sln.isAnagram_sort, s, t, expected)


if __name__ == "__main__":
    test_solution(s="anagram", t="nagaram", expected=True)
    test_solution(s="rat", t="car", expected=False)