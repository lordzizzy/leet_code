# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3744/

# Valid Number
# A valid number can be split up into these components (in order):

# A decimal number or an integer.
# (Optional) An 'e' or 'E', followed by an integer.
# A decimal number can be split up into these components (in order):

# (Optional) A sign character (either '+' or '-').
# One of the following formats:
# At least one digit, followed by a dot '.'.
# At least one digit, followed by a dot '.', followed by at least one digit.
# A dot '.', followed by at least one digit.
# An integer can be split up into these components (in order):

# (Optional) A sign character (either '+' or '-').
# At least one digit.
# For example, all the following are valid numbers: ["2", "0089", "-0.1",
# "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93",
# "-123.456e789"], while the following are not valid numbers: ["abc", "1a",
# "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].


# Given a string s, return true if s is a valid number.

# Example 1:
# Input: s = "0"
# Output: true

# Example 2:
# Input: s = "e"
# Output: false

# Example 3:
# Input: s = "."
# Output: false

# Example 4:
# Input: s = ".1"
# Output: true
#

# Constraints:
# 1 <= s.length <= 20
# s consists of only English letters (both uppercase and lowercase), digits
# (0-9), plus '+', minus '-', or dot '.'.

from typing import Callable
from termcolor import colored


class Solution:
    def isNumber(self, s: str) -> bool:
        return self.isNumber_first_attempt(s)

    def isNumber_first_attempt(self, s: str) -> bool:
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        def is_int(num: str) -> bool:
            num = num[1:] if len(num) > 1 and (num[0] == "+" or num[0] == "-") else num
            return all(c in digits for c in num)

        def is_decimal(num: str) -> bool:
            res = num.split(".")
            if len(res) == 1:
                return is_int(num)
            elif len(res) == 2:
                if res[0] or res[1]:
                    if is_int(res[0]) and all(c in digits for c in res[1]):
                        return True
                    else:
                        return (
                            len(res[1]) > 0
                            and (res[0] == "-" or res[0] == "+")
                            and all(c in digits for c in res[1])
                        )
                else:
                    return False
            else:
                return False

        r = s.lower().split("e")

        if len(r) == 1:
            return is_decimal(r[0])
        elif len(r) == 2:
            if r[0] and r[1]:
                return is_decimal(r[0]) and is_int(r[1])
            else:
                return False
        else:
            return False

    # https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA
    def isNumber_dfa(self, s: str) -> bool:
        currentState = 0
        state = [
            {"blank": 0, "sign": 1, "digit": 2, ".": 3},
            {"digit": 2, ".": 3},
            {"digit": 2, ".": 4, "e": 5, "blank": 8},
            {"digit": 4},
            {"digit": 4, "e": 5, "blank": 8},
            {"sign": 6, "digit": 7},
            {"digit": 7},
            {"digit": 7, "blank": 8},
            {"blank": 8},
        ]

        for c in s:
            if c == "E":
                c = "e"
            elif c >= "0" and c <= "9":
                c = "digit"
            elif c == " ":
                c = "blank"
            elif c in ["+", "-"]:
                c = "sign"
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        if currentState not in [2, 4, 7, 8]:
            return False
        return True

    def isNumber_pattern_match(self, s: str) -> bool:
        valid = [
            "xd",
            "x.d",
            "xd.",
            "xd.d",
            "xsd",
            "xsd.",
            "xsd.d",
            "xded",
            "x.ded",
            "xd.ed",
            "xd.ded",
            "xsded",
            "xsd.ed",
            "xsd.ded",
            "xdesd",
            "x.desd",
            "xd.esd",
            "xd.desd",
            "xsdesd",
            "xsd.esd",
            "xsd.desd",
            "xs.d",
            "xs.ed",
            "xs.esd",
            "xs.ded",
            "xs.desd",
        ]

        pat = "x"
        for _, ch in enumerate(s):
            if ch == "+" or ch == "-":
                pat = pat + "s"
            elif ch == "e" or ch == "E":
                pat = pat + "e"
            elif ch.isdigit():
                if pat[-1] != "d":
                    pat = pat + "d"
            elif ch == ".":
                pat = pat + "."
            else:
                return False

        return pat in valid


SolutionFunc = Callable[[str], bool]


def test_solution(s: str, expected: bool) -> None:
    def test_impl(func: SolutionFunc, s: str, expected: bool) -> None:
        r = func(s)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {s} is a valid number is {r}", "green"
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {s} is a valid number is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.isNumber_first_attempt, s, expected)
    test_impl(sln.isNumber_dfa, s, expected)
    test_impl(sln.isNumber_pattern_match, s, expected)


if __name__ == "__main__":
    test_solution(s="2", expected=True)
    test_solution(s="0089", expected=True)
    test_solution(s="-0.1", expected=True)
    test_solution(s="+3.14", expected=True)
    test_solution(s="4.", expected=True)
    test_solution(s="-.9", expected=True)
    test_solution(s="2e10", expected=True)
    test_solution(s="-90E3", expected=True)
    test_solution(s="3e+7", expected=True)
    test_solution(s="+6e-1", expected=True)
    test_solution(s="53.5e93", expected=True)
    test_solution(s="-123.456e789", expected=True)

    test_solution(s="abc", expected=False)
    test_solution(s="1a", expected=False)
    test_solution(s="1e", expected=False)
    test_solution(s="e3", expected=False)
    test_solution(s="99e2.5", expected=False)
    test_solution(s="--6", expected=False)
    test_solution(s="-+3", expected=False)
    test_solution(s="95a54e53", expected=False)

    test_solution(s="0", expected=True)
    test_solution(s="e", expected=False)
    test_solution(s=".", expected=False)
    test_solution(s=".1", expected=True)

    test_solution(s=".8+", expected=False)
    test_solution(s=".+", expected=False)
    test_solution(s="+.", expected=False)
