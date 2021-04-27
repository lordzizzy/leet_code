# # https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3722/

# Power of Three
# Given an integer n, return true if it is a power of three. Otherwise, return
# false.

# An integer n is a power of three, if there exists an integer x such that n ==
# 3x.

# Example 1:
# Input: n = 27
# Output: true

# Example 2:
# Input: n = 0
# Output: false

# Example 3:
# Input: n = 9
# Output: true

# Example 4:
# Input: n = 45
# Output: false


# Constraints:
# -231 <= n <= 231 - 1

# Follow up: Could you solve it without loops/recursion?

# https://leetcode.com/problems/power-of-three/solution/

from typing import Callable
from termcolor import colored

import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return self.isPowerOfThree_int_limitations(n)

    def isPowerOfThree_int_limitations(self, n: int) -> bool:
        return n > 0 and 3 ** 19 % n == 0

    def isPowerOfThree_iterative(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

    def isPowerOfThree_log(self, n: int) -> bool:
        return (math.log10(n) / math.log10(3)) % 1 == 0


SolutionFunc = Callable[[int], bool]


def test_solution(n: int, expected: bool) -> None:
    def test_impl(func: SolutionFunc, n: int, expected: bool) -> None:
        r = func(n)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {n} is a power of 3 is {r}", "green"
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {n} is a power of 3 is {r}, but expected is {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.isPowerOfThree_int_limitations, n, expected)
    test_impl(sln.isPowerOfThree_iterative, n, expected)
    test_impl(sln.isPowerOfThree_log, n, expected)


if __name__ == "__main__":
    test_solution(n=27, expected=True)
    test_solution(n=1024, expected=False)
