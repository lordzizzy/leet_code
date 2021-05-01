# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/597/week-5-april-29th-april-30th/3726/

# Given three integers x, y, and bound, return a list of all the powerful
# integers that have a value less than or equal to bound.

# An integer is powerful if it can be represented as x**i + y**j  for some integers
# i >= 0 and j >= 0.

# You may return the answer in any order. In your answer, each value should
# occur at most once.

# Example 1:
# Input: x = 2, y = 3, bound = 10
# Output: [2,3,4,5,7,9,10]
# Explanation:
# 2 = 20 + 30
# 3 = 21 + 30
# 4 = 20 + 31
# 5 = 21 + 31
# 7 = 22 + 31
# 9 = 23 + 30
# 10 = 20 + 32

# Example 2:
# Input: x = 3, y = 5, bound = 15
# Output: [2,4,6,8,10,14]

# Constraints:
# 1 <= x, y <= 100
# 0 <= bound <= 10⁶

from typing import Callable, List, Set
from termcolor import colored

import math


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        return self.powerfulIntegers_brute_force(x, y, bound)

    def powerfulIntegers_brute_force(self, x: int, y: int, bound: int) -> List[int]:
        a = bound if x == 1 else int(math.log(bound, x))
        b = bound if y == 1 else int(math.log(bound, y))

        s: Set[int] = set()

        for i in range(a + 1):
            for j in range(b + 1):
                value = x ** i + y ** j
                if value <= bound:
                    s.add(value)
                if y == 1:
                    break
            if x == 1:
                break

        return list(s)


SolutionFunc = Callable[[int, int, int], List[int]]


def test_solution(x: int, y: int, bound: int, expected: List[int]) -> None:
    def test_impl(
        func: SolutionFunc, x: int, y: int, bound: int, expected: List[int]
    ) -> None:
        r = func(x, y, bound)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => List of powerful integers from x={x}, y={y} and bound={bound} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => List of powerful integers from x={x}, y={y} and bound={bound} is {r}, but expected is {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.powerfulIntegers, x, y, bound, expected)


if __name__ == "__main__":
    test_solution(x=2, y=3, bound=10, expected=[2, 3, 4, 5, 7, 9, 10])
    test_solution(x=3, y=5, bound=15, expected=[2, 4, 6, 8, 10, 14])
