# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3736/

# Super Palindromes
# Let's say a positive integer is a super-palindrome if it is a palindrome, and
# it is also the square of a palindrome.

# Given two positive integers left and right represented as strings, return the
# number of super-palindromes integers in the inclusive range [left, right].

# Example 1:
# Input: left = "4", right = "1000"
# Output: 4
# Explanation: 4, 9, 121, and 484 are superpalindromes.
# Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a
# palindrome.

# Example 2:
# Input: left = "1", right = "2"
# Output: 1

# Constraints:
# 1 <= left.length, right.length <= 18
# left and right consist of only digits.
# left and right cannot have leading zeros.
# left and right represent integers in the range [1, 10¹⁸].
# left is less than or equal to right.

# https://leetcode.com/problems/super-palindromes/solution/

from typing import Callable
from termcolor import colored


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        return self.superpalindromesInRange_math(left, right)

    def superpalindromesInRange_math(self, left: str, right: str) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        L, R = int(left), int(right)
        MAGIC = 10 ** 5
        cnt = 0

        # odd
        for k in range(MAGIC):
            s = str(k)
            t = s + s[-2::-1]
            v = int(t) ** 2
            if v > R:
                break
            if v >= L and is_palindrome(str(v)):
                cnt += 1

        # even
        for k in range(MAGIC):
            s = str(k)
            t = s + s[::-1]
            v = int(t) ** 2
            if v > R:
                break
            if v >= L and is_palindrome(str(v)):
                cnt += 1

        return cnt

    # https://leetcode.com/discuss/explore/may-leetcoding-challenge-2021/1197698/super-palindromes-js-python-java-c-two-fast-mathematical-solutions-w-explanation
    # very interesting solution using base3 from the observation that:
    # x * x is a palindrome, then x is made up of only {0,1,2} as digits.

SolutionFunc = Callable[[str, str], int]


def test_solution(left: str, right: str, expected: int) -> None:
    def test_impl(func: SolutionFunc, left: str, right: str, expected: int) -> None:
        r = func(left, right)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Super palindromes in the range of {left} and {right} are {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Super palindromes in the range of {left} and {right} are {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.superpalindromesInRange_math, left, right, expected)


if __name__ == "__main__":
    test_solution(left="4", right="1000", expected=4)
    test_solution(left="1", right="2", expected=1)
    test_solution(left="40000000000000000", right="50000000000000000", expected=2)
