# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3799/

# Gray Code
# An n-bit gray code sequence is a sequence of 2n integers where:

# Every integer is in the inclusive range [0, 2n - 1],
# The first integer is 0,
# An integer appears no more than once in the sequence,
# The binary representation of every pair of adjacent integers differs by exactly one bit, and
# The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.


# Example 1:
# Input: n = 2
# Output: [0,1,3,2]
# Explanation:
# The binary representation of [0,1,3,2] is [00,01,11,10].
# - 00 and 01 differ by one bit
# - 01 and 11 differ by one bit
# - 11 and 10 differ by one bit
# - 10 and 00 differ by one bit
# [0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
# - 00 and 10 differ by one bit
# - 10 and 11 differ by one bit
# - 11 and 01 differ by one bit
# - 01 and 00 differ by one bit

# Example 2:
# Input: n = 1
# Output: [0,1]


# Constraints:
# 1 <= n <= 16

from typing import Callable, List
from termcolor import colored


class Solution:
    # Time complexity: O(2^N)
    # Space complexity: O(N)
    def grayCode_recursion(self, n: int) -> List[int]:
        ans: List[int] = []

        def generate(arr: List[int], n: int) -> List[int]:
            if n == 0:
                arr.append(0)
                return arr
            arr = generate(arr, n - 1)
            mask = 1 << (n - 1)
            for i in reversed(range(len(arr))):
                arr.append(arr[i] | mask)
            return arr

        return generate(ans, n)

    # Time complexity: O(2^N)
    # Space complexity: O(1)
    def grayCode_iterative_2loops(self, n: int) -> List[int]:
        ans: List[int] = [0]

        for i in range(1, n + 1):
            mask = 1 << (i - 1)
            for j in reversed(range(len(ans))):
                ans.append(ans[j] | mask)

        return ans

    # Time complexity: O(2^N)
    # Space complexity: O(1)
    def grayCode_iterative_1loop_optimized(self, n: int) -> List[int]:
        return [i ^ i >> 1 for i in range(1 << n)]


SolutionFunc = Callable[[int], List[int]]


def test_solution(n: int, expected: List[int]) -> None:
    def test_impl(func: SolutionFunc, n: int, expected: List[int]) -> None:
        r = func(n)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Valid n-bit gray code sequence for {n} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Valid n-bit gray code sequence for {n} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.grayCode_recursion, n, expected)
    test_impl(sln.grayCode_iterative_2loops, n, expected)
    test_impl(sln.grayCode_iterative_1loop_optimized, n, expected)


if __name__ == "__main__":
    test_solution(n=2, expected=[0, 1, 3, 2])
    test_solution(n=1, expected=[0, 1])
