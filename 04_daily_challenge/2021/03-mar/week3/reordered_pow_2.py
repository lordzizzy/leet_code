# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3679/

# Reordered Power of 2
# Starting with a positive integer N, we reorder the digits in any order
# (including the original order) such that the leading digit is not zero.

# Return true if and only if we can do this in a way such that the resulting
# number is a power of 2.

# Example 1:
# Input: 1
# Output: true

# Example 2:
# Input: 10
# Output: false

# Example 3:
# Input: 16
# Output: true

# Example 4:
# Input: 24
# Output: false

# Example 5:
# Input: 46
# Output: true

# Note:
# 1 <= N <= 10⁹

import collections
import itertools
from typing import Callable, Generator, Set
from termcolor import colored


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        return self.reorderedPowerOf2_count_digits(N)

    def reorderedPowerOf2_count_digits(self, N: int) -> bool:
        c = collections.Counter(str(N))
        return any(c == collections.Counter(str(1 << i)) for i in range(30))

    def reorderedPowerOf2_count_digits_cpp_style(self, N: int) -> bool:
        def counter(n: int) -> int:
            res = 0
            while n:
                res += pow(10, n % 10)
                n //= 10
            return res

        N = counter(N)
        for i in range(32):
            if counter(1 << i) == N:
                return True

        return False

    def reorderedPowerOf2_sort_and_check(self, N: int) -> bool:
        S: Set[str] = {
            "1",
            "2",
            "4",
            "8",
            "16",
            "23",
            "46",
            "128",
            "256",
            "125",
            "0124",
            "0248",
            "0469",
            "1289",
            "13468",
            "23678",
            "35566",
            "011237",
            "122446",
            "224588",
            "0145678",
            "0122579",
            "0134449",
            "0368888",
            "11266777",
            "23334455",
            "01466788",
            "112234778",
            "234455668",
            "012356789",
        }
        s = "".join(sorted(str(N)))
        return s in S

    # this is slower than counter/sort method, just here for learning about how
    # to generate proper permutations in python and other lang just in case we
    # need it in the future
    def reorderedPowerOf2_permutations_lib(self, N: int) -> bool:
        for s in itertools.permutations(str(N)):
            if s[0] != "0" and bin(int("".join(s))).count("1") == 1:
                return True
        return False

    def reorderedPowerOf2_permutations_manual(self, N: int) -> bool:
        def permutate(S: str) -> Generator[str, None, None]:
            n = len(S)
            if n <= 1:
                yield S
            else:
                for i in range(n):
                    S1 = S[:i]
                    S2 = S[i + 1 :]
                    for p in permutate(S1 + S2):
                        s = S[i] + p
                        yield s

        for s in permutate(str(N)):
            if s[0] != "0" and bin(int("".join(s))).count("1") == 1:
                return True
        return False


SolutionFunc = Callable[[int], bool]


def test_solution(N: int, expected: bool) -> None:
    def test_impl(func: SolutionFunc, N: int, expected: bool) -> None:
        r = func(N)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => {N} can be reordered to power of 2 is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => {N} can be reordered to power of 2 is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.reorderedPowerOf2_count_digits, N, expected)
    test_impl(sln.reorderedPowerOf2_count_digits_cpp_style, N, expected)
    test_impl(sln.reorderedPowerOf2_sort_and_check, N, expected)
    test_impl(sln.reorderedPowerOf2_permutations_lib, N, expected)
    test_impl(sln.reorderedPowerOf2_permutations_manual, N, expected)


if __name__ == "__main__":
    test_solution(N=1234, expected=False)
    test_solution(N=1, expected=True)
    test_solution(N=10, expected=False)
    test_solution(N=16, expected=True)
    test_solution(N=24, expected=False)
    test_solution(N=46, expected=True)
