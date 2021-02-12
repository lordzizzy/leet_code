# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3637/

# Number of Steps to Reduce a Number to Zero
# Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

# Example 1:
# Input: num = 14
# Output: 6
# Explanation:
# Step 1) 14 is even; divide by 2 and obtain 7.
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3.
# Step 4) 3 is odd; subtract 1 and obtain 2.
# Step 5) 2 is even; divide by 2 and obtain 1.
# Step 6) 1 is odd; subtract 1 and obtain 0.

# Example 2:
# Input: num = 8
# Output: 4
# Explanation:
# Step 1) 8 is even; divide by 2 and obtain 4.
# Step 2) 4 is even; divide by 2 and obtain 2.
# Step 3) 2 is even; divide by 2 and obtain 1.
# Step 4) 1 is odd; subtract 1 and obtain 0.

# Example 3:
# Input: num = 123
# Output: 12

# Constraints:
# 0 <= num <= 10⁶

from __future__ import annotations
from typing import Callable
from termcolor import colored


class Solution:
    def numberOfSteps(self, num: int) -> int:
        return self.numberOfSteps_naive(num)

    def numberOfSteps_naive(self, num: int) -> int:
        steps = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            steps += 1
        return steps


SolutionFunc = Callable[[int], int]


def test_solution(num: int, expected: int):
    def test_impl(func: SolutionFunc, num: int, expected: int):
        r = func(num)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => number of steps to reduce {num} to 0 is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => number of steps to reduce {num} to 0 is {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.numberOfSteps, num, expected)


if __name__ == "__main__":
    test_solution(num=0, expected=0)
    test_solution(num=14, expected=6)
    test_solution(num=8, expected=4)
    test_solution(num=123, expected=12)
    test_solution(num=997, expected=16)