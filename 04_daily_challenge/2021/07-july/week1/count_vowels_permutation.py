# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3802/

# Count Vowels Permutation

# Solution
# Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
# Since the answer may be too large, return it modulo 10^9 + 7.


# Example 1:
# Input: n = 1
# Output: 5
# Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

# Example 2:
# Input: n = 2
# Output: 10
# Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io",
# "iu", "oi", "ou" and "ua".

# Example 3:
# Input: n = 5
# Output: 68

# Constraints:

# 1 <= n <= 2 * 10⁴

from functools import lru_cache
from typing import Callable, List

import numpy as np
from termcolor import colored


class Solution:
    # Time complexity: O(N)
    # Space complexity: O(1)
    def countVowelPermutation_dp_bottomup(self, n: int) -> int:
        a = e = i = o = u = 1

        for _ in range(1, n):
            a, e, i, o, u = (
                (e + u + i),
                (a + i),
                (e + o),
                i,
                (o + i),
            )

        return (a + e + i + o + u) % (10 ** 9 + 7)

    # Time complexity: O(N)
    # Space complexity: O(5*N) = O(N)
    def countVowelPermutation_dp_topdown(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def count_vowel(i: int, vowel: str) -> int:
            total = 1
            if i > 1:
                if vowel == "a":
                    total = (
                        count_vowel(i - 1, "e")
                        + count_vowel(i - 1, "u")
                        + count_vowel(i - 1, "i")
                    )
                elif vowel == "e":
                    total = count_vowel(i - 1, "a") + count_vowel(i - 1, "i")
                elif vowel == "i":
                    total = count_vowel(i - 1, "e") + count_vowel(i - 1, "o")
                elif vowel == "o":
                    total = count_vowel(i - 1, "i")
                else:
                    total = count_vowel(i - 1, "i") + count_vowel(i - 1, "o")
            return total

        return sum(count_vowel(n, vowel) for vowel in "aeiou") % (10 ** 9 + 7)

    # reference
    # https://leetcode.com/problems/count-vowels-permutation/discuss/1315077/Python-2-solution%3A-dp-and-matrix-power-explained
    #
    # Time complexity:  O(5**3 * logN) = O(logN)
    # Space complexity: O(5*5 N) - O(N)
    def countVowelPermutation_power_of_matrices(self, n: int) -> int:
        MAX = 10 ** 9 + 7

        def power(mat: List[List[int]], n: int) -> int:
            result = np.eye(len(mat), dtype=int)
            while n > 0:
                if n % 2:
                    result = np.dot(mat, result) % MAX
                mat = np.dot(mat, mat) % MAX
                n //= 2
            return result

        mat = np.matrix(
            [
                [0, 1, 0, 0, 0],  # a -> e
                [1, 0, 1, 0, 0],  # e -> a, i
                [1, 1, 0, 1, 1],  # i -> a, e, o, u
                [0, 0, 1, 0, 1],  # o -> i, u
                [1, 0, 0, 0, 0],  # u -> a
            ]
        )
        return np.sum(power(mat, n - 1)) % MAX


SolutionFunc = Callable[[int], int]


def test_solution(n: int, expected: int) -> None:
    def test_impl(func: SolutionFunc, n: int, expected: int) -> None:
        r = func(n)
        if r == expected:
            print(
                colored(
                    f"PASSED {func.__name__} => Count permutations of vowel string with length {n} is {r}",
                    "green",
                )
            )
        else:
            print(
                colored(
                    f"FAILED {func.__name__} => Count permutations of vowel string with length {n} is {r} but expected {expected}",
                    "red",
                )
            )

    sln = Solution()
    test_impl(sln.countVowelPermutation_dp_bottomup, n, expected)
    test_impl(sln.countVowelPermutation_dp_topdown, n, expected)
    test_impl(sln.countVowelPermutation_power_of_matrices, n, expected)


if __name__ == "__main__":
    test_solution(n=1, expected=5)
    test_solution(n=2, expected=10)
    test_solution(n=3, expected=19)
    test_solution(n=5, expected=68)
