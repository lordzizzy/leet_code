# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3756/

# Partitioning Into Minimum Number Of Deci-Binary Numbers
# A decimal number is called deci-binary if each of its digits is either 0 or 1
# without any leading zeros. For example, 101 and 1100 are deci-binary, while
# 112 and 3001 are not.

# Given a string n that represents a positive decimal integer, return the
# minimum number of positive deci-binary numbers needed so that they sum up to
# n.

# Example 1:
# Input: n = "32"
# Output: 3
# Explanation: 10 + 11 + 11 = 32

# Example 2:
# Input: n = "82734"
# Output: 8

# Example 3:
# Input: n = "27346209830709182346"
# Output: 9

# Constraints:

# 1 <= n.length <= 10⁵
# n consists of only digits.
# n does not contain any leading zeros and represents a positive integer.

from typing import Callable
from termcolor import colored


class Solution:
    def minPartitions(self, n: str) -> int:
        return self.minPartitions_set(n)

    def minPartitions_first(self, n: str) -> int:
        ans = 0
        for c in n:
            ans = max(ans, int(c))
            if ans == 9:
                break
        return ans

    def minPartitions_set(self, n: str) -> int:
        return int(max(n))

    def minPartitions_fast(self, n: str) -> int:
        for num in range(9, 0, -1):
            if str(num) in n:
                return num
        return 0


SolutionFunc = Callable[[str], int]


def test_solution(n: str, expected: int) -> None:
    def test_impl(func: SolutionFunc, n: str, expected: int) -> None:
        r = func(n)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Min number of deci-binary partitions for {n} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Min number of deci-binary partitions for {n} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.minPartitions_first, n, expected)
    test_impl(sln.minPartitions_set, n, expected)
    test_impl(sln.minPartitions_fast, n, expected)


if __name__ == "__main__":
    test_solution(n="32", expected=3)
    test_solution(n="82734", expected=8)
    test_solution(n="27346209830709182346", expected=9)
