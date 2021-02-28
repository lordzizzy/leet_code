# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3654/

# Divide Two Integers
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division, and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero, which means losing its
# fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

# Note:
# Assume we are dealing with an environment that could only store integers
# within the 32-bit signed integer range: [−2³¹,  2³¹ − 1]. For this problem,
# assume that your function returns 2³¹ − 1 when the division result overflows.

# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = truncate(3.33333..) = 3.

# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = truncate(-2.33333..) = -2.

# Example 3:
# Input: dividend = 0, divisor = 1
# Output: 0

# Example 4:
# Input: dividend = 1, divisor = 1
# Output: 1

# Constraints:
# -2³¹ <= dividend, divisor <= 2³¹ - 1
# divisor != 0

# sample 12ms submission
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         res, flag = 0, 0
#         if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
#             flag = -1
#         dividend, divisor = abs(dividend), abs(divisor)
#         while dividend >= divisor:
#             n = 0
#             while dividend >= divisor << n:
#                 n += 1
#             res += 1 << (n - 1)
#             dividend -= (divisor << (n-1))
#         res = -res if flag == -1 else res
#         if res < -2147483648 or res > 2147483647:
#             return 2147483647
#         return res

from typing import Callable
from termcolor import colored


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return self.divide_sub_loop(dividend, divisor)

    def divide_sub_loop(self, dividend: int, divisor: int) -> int:
        # handle overflow case for -2³¹ / 1
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        dv = int(abs(dividend))
        ds = int(abs(divisor))
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        res = 0

        for x in reversed(range(32)):
            if (dv >> x) - ds >= 0:
                res += 1 << x
                dv -= ds << x

        return res * sign


SolutionFunc = Callable[[int, int], int]


def test_solution(dividend: int, divisor: int, expected: int) -> None:
    def test_impl(
        func: SolutionFunc, dividend: int, divisor: int, expected: int
    ) -> None:
        r = func(dividend, divisor)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {dividend} // {divisor} = {r}", "green"
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {dividend} // {divisor} = {r}, but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.divide_sub_loop, dividend, divisor, expected)


if __name__ == "__main__":
    test_solution(dividend=-2147483648, divisor=-1, expected=2147483647)
    test_solution(dividend=10, divisor=3, expected=3)
    test_solution(dividend=7, divisor=-3, expected=-2)
    test_solution(dividend=2, divisor=2, expected=1)
    test_solution(dividend=0, divisor=1, expected=0)
    test_solution(dividend=-1, divisor=1, expected=-1)
    test_solution(dividend=-1, divisor=-1, expected=1)
    test_solution(dividend=1, divisor=1, expected=1)