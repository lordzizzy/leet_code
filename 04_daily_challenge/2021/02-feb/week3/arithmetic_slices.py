# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3644/

# Arithmetic Slices
# A sequence of numbers is called arithmetic if it consists of at least three
# elements and if the difference between any two consecutive elements is the
# same.

# For example, these are arithmetic sequences:
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9

# # The following sequence is not arithmetic.
# 1, 1, 2, 5, 7

# A zero-indexed array A consisting of N numbers is given. A slice of that
# array is any pair of integers (P, Q) such that 0 <= P < Q < N.

# A slice (P, Q) of the array A is called arithmetic if the sequence:
# A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means
# that P + 1 < Q.

# The function should return the number of arithmetic slices in the array A.


# Example:
# A = [1, 2, 3, 4]
# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3,
# 4] itself.

from typing import Callable, List
from termcolor import colored


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        return self.numberOfArithmeticSlices_better_bf(A)

    def numberOfArithmeticSlices_better_bf(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        res = 0
        diff = A[0] - A[1]
        last = 0
        count = 1
        for i in range(1, n - 1):
            d = A[i] - A[i + 1]
            if diff != d:
                diff = d
                if i - last >= 2:
                    s = i - last + 1
                    res += sum((s - i) + 1 for i in range(3, s + 1))
                last = i
                count = 1
            else:
                count += 1
        if count >= 2:
            res += sum((n - last - i) + 1 for i in range(3, n - last + 1))
        return res

    def numberOfArithmeticSlices_dp(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        dp = [0] * n
        sum = 0
        for i in range(2, n):
            if A[i - 2] - A[i - 1] == A[i - 1] - A[i]:
                dp[i] = 1 + dp[i - 1]
                sum += dp[i]
        return sum

    def numberOfArithmeticSlices_dp_o1_mem(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        dp = 0
        sum = 0
        for i in range(2, n):
            if A[i - 2] - A[i - 1] == A[i - 1] - A[i]:
                dp = 1 + dp
                sum += dp
            else:
                dp = 0
        return sum

    def numberOfArithmeticSlices_formula(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        count = 0
        sum = 0
        for i in range(2, n):
            if A[i - 2] - A[i - 1] == A[i - 1] - A[i]:
                count += 1
            else:
                sum += count * (count + 1) // 2
                count = 0
        sum += count * (count + 1) // 2
        return sum


SolutionFunc = Callable[[List[int]], int]


def test_solution(A: List[int], expected: int) -> None:
    def test_impl(func: SolutionFunc, A: List[int], expected: int) -> None:
        r = func(A)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => number of arithmetic slices in {A} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => number of arithmetic slices in {A} is {r}, but expected: {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.numberOfArithmeticSlices_better_bf, A, expected)
    test_impl(sln.numberOfArithmeticSlices_dp, A, expected)
    test_impl(sln.numberOfArithmeticSlices_dp_o1_mem, A, expected)
    test_impl(sln.numberOfArithmeticSlices_formula, A, expected)


if __name__ == "__main__":
    test_solution(A=[1, 2, 3, 4], expected=3)
    test_solution(A=[1, 2, 3], expected=1)
    test_solution(A=[1, 2, 3, 5], expected=1)
    test_solution(A=[1, 1, 2, 5, 7], expected=0)
    test_solution(A=[1, 2, 3, 8, 9, 10], expected=2)
