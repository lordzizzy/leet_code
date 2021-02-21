# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3646/

# Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added
# together. 12 is written as XII, which is simply X + II. The number 27 is
# written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3
# Example 2:

# Input: s = "IV"
# Output: 4
# Example 3:

# Input: s = "IX"
# Output: 9
# Example 4:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 5:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

from typing import Callable
from termcolor import colored


class Solution:
    def romanToInt(self, s: str) -> int:
        return self.romanToInt_forward(s)

    def romanToInt_forward(self, s: str) -> int:
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        res = 0
        ch = s[0]
        i = 1
        cnt = 1
        while i < n:
            if ch == s[i]:
                cnt += 1
            elif map[ch] < map[s[i]]:
                res += map[s[i]] - map[ch]
                if i + 1 < n:
                    ch = s[i + 1]
                    cnt = 1
                    i += 1
                else:
                    cnt = 0
            else:
                res += map[ch] * cnt
                ch = s[i]
                cnt = 1
            i += 1
        if cnt > 0:
            res += map[ch] * cnt
        return res

    def romanToInt_backward(self, s: str) -> int:
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        res = 0
        prev = -1
        for i in reversed(range(n)):
            cur = map[s[i]]
            if prev > cur:
                cur *= -1
            res += cur
            prev = cur
        return res


SolutionFunc = Callable[[str], int]


def test_solution(s: str, expected: int) -> None:
    def test_impl(func: SolutionFunc, s: str, expected: int) -> None:
        r = func(s)
        if r == expected:
            print(colored(f"PASSED {func.__name__} => {s} to int is {r}", "green"))
        else:
            print(
                colored(
                    f"WORD {func.__name__} => {s} to int is {r}, but expected is {expected}",
                    "red",
                )
            )

    sln = Solution()
    # test_impl(sln.romanToInt_forward, s, expected)
    test_impl(sln.romanToInt_backward, s, expected)


if __name__ == "__main__":
    # test_solution(s="III", expected=3)
    # test_solution(s="IV", expected=4)
    # test_solution(s="LVIII", expected=58)
    # test_solution(s="MCMXCIV", expected=1994)
    # test_solution(s="LVI", expected=56)
    test_solution(s="MMMCMXCVIII", expected=3998)
