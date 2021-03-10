# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3667/

# Integer to Roman
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
# Given an integer, convert it to a roman numeral.

# Example 1:
# Input: num = 3
# Output: "III"

# Example 2:
# Input: num = 4
# Output: "IV"

# Example 3:
# Input: num = 9
# Output: "IX"

# Example 4:
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.

# Example 5:
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Constraints:
# 1 <= num <= 3999

from typing import Callable, Dict, List
from termcolor import colored


class Solution:
    def intToRoman(self, num: int) -> str:
        return self.intToRoman_lookup(num)

    def intToRoman_lookup(self, num: int) -> str:
        s = str(num)
        n = len(s)
        d: Dict[int, str] = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            4: "IV",
            40: "XL",
            400: "CD",
            9: "IX",
            90: "XC",
            900: "CM",
        }
        res: List[str] = []

        for i, char in enumerate(s, 1):
            base = 10 ** (n - i)
            v = int(char)

            if v == 0:
                continue
            elif v <= 3:
                res.extend([d[base]] * v)
            elif v == 4 or v == 9:
                res.append(d[v * base])
            else:
                res.append(d[5 * base])
                if v - 5:
                    res.extend([d[base]] * (v - 5))

            # print(f"v={v}, key={base} => {v * base}")

        return "".join(res)

    def intToRoman_lookup_divmod(self, num: int) -> str:
        digits = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        roman = ""
        for key in digits:
            value = digits[key]
            if num == 0:
                break
            count, num = divmod(num, key)
            roman += value * count
        return roman

    def intToRoman_elegant(self, num: int) -> str:
        d = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        res = ""

        for i in d:
            res += (num // i) * d[i]
            num %= i

        return res


SolutionFunc = Callable[[int], str]


def test_solution(num: int, expected: str) -> None:
    def test_impl(func: SolutionFunc, num: int, expected: str) -> None:
        r = func(num)
        if r == expected:
            print(colored(f"PASSED {func.__name__} => {num} in roman is {r}", "green"))
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {num} in roman is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.intToRoman_lookup, num, expected)
    test_impl(sln.intToRoman_lookup_divmod, num, expected)
    test_impl(sln.intToRoman_elegant, num, expected)


if __name__ == "__main__":
    test_solution(num=3, expected="III")
    test_solution(num=4, expected="IV")
    test_solution(num=9, expected="IX")
    test_solution(num=58, expected="LVIII")
    test_solution(num=1994, expected="MCMXCIV")
    test_solution(num=3999, expected="MMMCMXCIX")
    test_solution(num=58, expected="LVIII")
    test_solution(num=40, expected="XL")
